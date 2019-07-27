from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter fullname'}))
    email    = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'enter email'}))
    message  = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'enter message content'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not 'gmail.com' in email:
            raise forms.ValidationError('Email has to be gmail.com')
        return email

class LoginForm(forms.Form):
    username = forms.CharField( max_length=50)
    password = forms.CharField(max_length=50,widget= forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField( max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter username'}))
    email    =forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'enter email'}))
    password = forms.CharField(max_length=50, widget= forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',max_length=50, widget= forms.PasswordInput)

    #validation
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs      = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('username already exists')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs      = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('email already exists')
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError('password must be matched')
        return data
    

    
