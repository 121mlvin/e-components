import re
from .utils import load_components
from .forms import ComponentForm
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.utils.translation import gettext as _


def homepage(request):
    return render(request, 'homepage.html')


def check_component(request):
    result = None
    details = None
    if request.method == 'POST':
        form = ComponentForm(request.POST)
        if form.is_valid():
            component_input = form.cleaned_data['component'].strip().upper()
            match = re.match(r'(E?\s*?)(\d+)', component_input)

            if match:
                component = f"E{match.group(2)}"
                data = load_components()

                if component in data:
                    details = data[component]
                    result = _("Component %(component)s is categorized as %(category)s.") % {
                        'component': component,
                        'category': details['category']
                    }
                else:
                    result = _("Component %(component)s not found.") % {'component': component}
            else:
                result = _("Invalid component format.")
    else:
        form = ComponentForm()

    return render(request, 'check_component.html', {'form': form, 'result': result, 'details': details})


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        try:
            send_mail(
                subject=_("Message from %(name)s") % {'name': name},
                message=message,
                from_email=email,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
            )
            messages.success(request, _("Your message has been sent successfully!"))
        except Exception as e:
            messages.error(request, _("An error occurred while sending your message. Please try again later."))

        return render(request, 'contact_us.html')

    return render(request, 'contact_us.html')

