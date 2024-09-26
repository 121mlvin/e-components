from django import forms


class ComponentForm(forms.Form):
    component = forms.CharField(label='E Component', max_length=10, required=True)
