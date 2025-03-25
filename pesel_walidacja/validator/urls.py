from django.urls import path
from .views import pesel_validator_view

urlpatterns = [
    path('', pesel_validator_view, name='pesel_validator'),
]
