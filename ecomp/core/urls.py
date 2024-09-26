from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('check-component/', views.check_component, name='check_component'),
    path('contact/', views.contact_view, name='contact_us'),
]
