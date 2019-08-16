from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length=30, required=False, help_text='Optional.',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your first name'}))
    last_name = forms.CharField(label='Last Name', max_length=30, required=False, help_text='Optional.',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your last name'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your eamil'}))
    nid = forms.CharField(max_length=254, help_text='Required. Inform a valid nid address.',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your nid'}))
    bank = forms.CharField(max_length=254, help_text='Required. Inform a valid bank address.', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter bank accounts no.'}))
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','nid','bank', 'birth_date')
        widgets = {
            'username': forms.TextInput(
                attrs ={
                    'class': 'form-control',
                    'placeholder': 'enter a username'
                }
            ),
            'password1': forms.PasswordInput(
                attrs ={
                    'class': 'form-control',
                    'placeholder': 'enter password'
                }
            ),
            'password2': forms.PasswordInput(
                attrs ={
                    'class': 'form-control',
                    'placeholder': 'confirm password'
                }
            ),
            
        }



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


# Login
class LoginForm(forms.Form):
    username = forms.CharField( max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter username'}))
    password = forms.CharField(max_length=50,widget= forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))

class RegisterForm(forms.Form):
    username = forms.CharField( max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter username'}))
    email    =forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'enter email'}))
    password = forms.CharField(max_length=50, widget= forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    password2 = forms.CharField(label='Confirm-password',max_length=50, widget= forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm-password'}))

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
    

# Donation 


    

    



















# from django import forms
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class ContactForm(forms.Form):
#     fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter fullname'}))
#     email    = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'enter email'}))
#     message  = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'enter message content'}))

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if not 'gmail.com' in email:
#             raise forms.ValidationError('Email has to be gmail.com')
#         return email

# class LoginForm(forms.Form):
#     username = forms.CharField( max_length=50)
#     password = forms.CharField(max_length=50,widget= forms.PasswordInput)

# class RegisterForm(forms.Form):
#     first_name      = forms.CharField( max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter first name'}))
#     last_name       =forms.CharField( max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter last name'}))
#     username        = forms.CharField( max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter username'}))
#     email           =forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'enter email'}))
#     password        = forms.CharField(max_length=50, widget= forms.PasswordInput)
#     password2       = forms.CharField(label='Confirm Password',max_length=50, widget= forms.PasswordInput)
#     #nid             =forms.CharField( max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your nid number'}))
#     #bank_account    =forms.CharField( max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter bank account number'}))
#     #phone_number    = forms.CharField( max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter phone number'}))

    

#     #validation
#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         qs      = User.objects.filter(username=username)
#         if qs.exists():
#             raise forms.ValidationError('username already exists')
#         return username
    
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         qs      = User.objects.filter(email=email)
#         if qs.exists():
#             raise forms.ValidationError('email already exists')
#         return email

#     def clean(self):
#         data = self.cleaned_data
#         password = self.cleaned_data.get('password')
#         password2 = self.cleaned_data.get('password2')
#         if password2 != password:
#             raise forms.ValidationError('password must be matched')
#         return data
    

    


# users/forms.py
# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):
#     nid             =forms.CharField( max_length=50, widget=forms.TextInput())
#     bank_account    =forms.CharField( max_length=50, widget=forms.TextInput())
#     phone_number    = forms.CharField( max_length=50, widget=forms.TextInput())

#     class Meta(UserCreationForm):
#         model = CustomUser
#         fields = ('fullname','username', 'email','nid','bank_account','phone_number')

# class CustomUserChangeForm(UserChangeForm):
#     nid             =forms.CharField( max_length=50, widget=forms.TextInput())
#     bank_account    =forms.CharField( max_length=50, widget=forms.TextInput())
#     phone_number    = forms.CharField( max_length=50, widget=forms.TextInput())

#     class Meta:
#         model = CustomUser
#         fields = ('fullname','username', 'email','nid','bank_account','phone_number')