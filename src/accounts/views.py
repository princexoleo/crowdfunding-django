from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
#from accounts.models import User
from accounts.forms import SignUpForm, LoginForm, RegisterForm,ContactForm
#LoginForm


# Create your views here.
#login page function
User = get_user_model()

################
#working ....

# def login_view(request):
#     form  = SignUpForm(request.POST or None)
#     print(request.user.is_authenticated)
#     context ={
#         'title':'Login',
#         'form': form,
#     }
#     if form.is_valid():
#         print(form.cleaned_data)
#         username = form.cleaned_data.get('username')
#         row_password = form.cleaned_data.get('password')
#         user = authenticate(request, username = username, password = row_password)
#         print(request.user.is_authenticated)
#         if user is not None:
#             print(request.user.is_authenticated)
#             login(request, user)
#             #context['form'] = LoginForm()
#             print('Redirect Success Page')
#             return redirect('home')
#         else:
#             print('Login Error')
#     return render(request, 'accounts/login_page.html', context)


# ###########

# #register page function
# #working ....
def complete_profile_view(request):
    #form  = RegisterForm(request.POST or None)
    context ={
        'title':'Register',
        # 'form': form,
    }
    return render(request, 'accounts/register.html', context)

# def register_view(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             print('success')
#             return redirect('home')
#     else:
#         form = SignUpForm()
#         return render(request, 'accounts/register_page.html', {'form': form})

#     return render(request, 'accounts/register_page.html', {'form': form})


# def register_view(request):
#     context ={
#         'title':'Register'
#     }
#     if request.method == 'POST':
#         print('register stated')
#         print(request.POST)
#         form = CustomUserCreationForm(request.POST or None)
#         form.save()
#         username = form.cleaned_data.get('username')
#         raw_password = form.cleaned_data.get('password')
#         user = authenticate(request,username=username, password=raw_password)
#         user.fullname = form.cleaned_data.get('fullname')
#         user.nid = form.cleaned_data.get('password')
#         user.phone_number = form.cleaned_data.get('phone_number')
#         user.bank_account = form.cleaned_data.get('bank_account')
#         user.fullname = form.cleaned_data.get('fullname')
#         login(request, user)
#         print('success')
#         return redirect('home')
#         #return redirect('register')
#     return render(request,'accounts/register.html',context)

# def register_view(request):
#     context ={
#         'title':'Register'
#     }
#     if request.method == 'POST':
#         form = SignUpForm(request.POST or None)
#         print(form)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()
#             user.profile.fullname = form.cleaned_data.get('fullname')
#             user.profile.username = form.cleaned_data.get('username')
#             user.profile.nid = form.cleaned_data.get('password')
#             user.profile.phone_number = form.cleaned_data.get('phone_number')
#             user.profile.bank_account = form.cleaned_data.get('bank_account')
#             user.save()
#             raw_password = form.cleaned_data.get('password')
#             user = authenticate(request,username=username, password=raw_password)
#             print('reg success')
#             print(user)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#         print('Failed to register')
#         return render(request,'accounts/register.html',context)

#     return render(request,'accounts/register.html',context)


#Home page function
def home_view(request):
    context ={
        'title':'Home'
    }
    return render(request,'accounts/home.html',context)

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('home')

def contact_view(request):
    contact_form = ContactForm(request.POST or None)
    context ={
        'title':'Contact',
        'form': contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == 'POST':
    #     print(request.POST)
    #     print(request.POST.get('fullname'))
    return render(request, 'contact.html', context)

def login_view(request):
    form  = LoginForm(request.POST or None)
    print(request.user.is_authenticated)
    context ={
        'title':'Login',
        'form': form,
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        row_password = form.cleaned_data.get('password')
        user = authenticate(request, username = username, password = row_password)
        print(request.user.is_authenticated)
        if user is not None:
            print(request.user.is_authenticated)
            login(request, user)
            #context['form'] = LoginForm()
            print('Redirect Success Page')
            return redirect('home')
        else:
            print('Login Error')
    return render(request, 'accounts/login_page.html', context)

User = get_user_model()
def register_view(request):
    form  = RegisterForm(request.POST or None)
    context ={
        'title':'Register',
        'form': form,
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        row_password = form.cleaned_data.get('password')
        User.objects.create_user(username=username, password=row_password)
        return redirect('login')
    return render(request, 'accounts/register_page.html', context)

def startup_view(request):
    context ={
        'title':'Register',
        
    }

    return render(request,'startup.html',context)

def hospital_view(request):
    context ={
        'title':'Register',
       
    }

    return render(request,'hospital.html',context)

def education_view(request):
    context ={
        'title':'Register',
        
    }

    return render(request,'education.html',context)