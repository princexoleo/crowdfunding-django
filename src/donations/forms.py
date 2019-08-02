from django import forms
from django.forms import ModelForm
from .models import Donation

class DonationForm(forms.ModelForm):

    class Meta:
        model = Donation
        fields = ['amount', 'purpose']
        exclude =['user']