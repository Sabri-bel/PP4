from django import forms
from .models import ReservationRequest


class ReservationForm(forms.ModelForm):
    """
    form class for request a reservation
    """
    class Meta:
        model = ReservationRequest
        fields = ('name', 'email', 'message')
