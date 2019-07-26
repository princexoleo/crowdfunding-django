from django.shortcuts import render

# Create your views here.
#login page function
def login_view(request):
    context ={
        'title':'Login'
    }
    return render(request,'accounts/login.html',context)


#register page function
def register_view(request):
    context ={
        'title':'Register'
    }
    return render(request,'accounts/register.html',context)


#Home page function
def home_view(request):
    context ={
        'title':'Home'
    }
    return render(request,'accounts/home.html',context)
