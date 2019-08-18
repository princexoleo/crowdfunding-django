from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,get_user_model,logout 
from .forms import LoginForm, RegisterForm,ContactForm, SignUpForm
from .models import Profile
from donations.models import Donation
#AJAX
#import json, pdb


# Create your views here
# login page function

User = get_user_model()


def complete_profile_view(request):
    #form  = RegisterForm(request.POST or None)
    context ={
        'title':'Register',
        # 'form': form,
    }
    return render(request, 'accounts/register.html', context)








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
    return render(request, 'dash/login-page.html', context)

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

def signup(request):
    context = {
        'form': 'null'
    }
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birthdate = form.cleaned_data.get('birth_date')
            user.profile.nid = form.cleaned_data.get('nid')
            user.profile.bank = form.cleaned_data.get('bank')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
        context['form']= form

    return render(request, 'dash/register_page.html', context)


def dashboard_view(request):
    user_instance = User.objects.get(pk=request.user.id)
    user_info = Profile.objects.get(user=user_instance)
    #print(user_instance)
    balance = user_info.account_balance
    context ={
         'status':'null',
         'user_balance': balance,
         'user_profile': user_info
    }
    try:
        #donation_status = Donation.objects.filter(user=user_instance).order_by('created_date').distinct()
        #donate_status = Donation.objects.filter(user=user_instance).values_list('status', flat=True).distinct()
        user_donation = Donation.objects.filter(user = user_instance).order_by('-created_date')
        context['history'] = Donation.objects.filter(user = user_instance).order_by('-created_date')
        if len(user_donation) > 0:
            context['status'] = user_donation[0].status
            if user_donation[0].status == True and user_donation[0].transaction_status == False:
                d_amount = user_donation[0].amount
                if user_donation[0].donate_type == 'RD':
                    balance+=d_amount
                    # update userprofile balance 
                    user_info.account_balance = balance
                    user_donation[0].transaction_status = True # Transaction completed
                elif user_donation[0].donate_type == 'GD':
                    if balance > 0 :
                        balance-=d_amount # check enough balance in account 
                        user_info.account_balance = balance
                        user_donation[0].transaction_status = True # Transaction completed
                user_info.save()
                context['msg'] = 'Accepted!!'
                context['user_balance'] = user_info.account_balance
            elif user_donation[0].transaction_status == True and user_donation[0].status == False:
                context['msg'] = 'Sorry your requested Rejected!!'
            else:
                context['msg'] = 'Pending'
        else :
            pass
        # print(donate_status[0])
        # context['status'] = donate_status[0]
    except Donation.DoesNotExists:
        context['status'] = False
        context['msg'] = 'You have not requested yet!!' 
    

    return render(request, 'dash/dashboard.html',context)


def comming_soon(request):
    return render(request,'message/comming_soon.html',{})
