from django import forms
from django.forms import ModelForm
from .models import Donation

class DonationForm(forms.ModelForm):

    class Meta:
        model = Donation
        fields = ['donate_type','amount', 'purpose']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'myfieldclass', 'placeholder':'enter amount'}),
            'purpose':forms.Select()
           
        }
        exclude =['user']