from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Donation
from .forms import DonationForm

# Create your views here.
def donation_view(request):
    form = DonationForm(request.POST)
    if form.is_valid():
            donation = form.save(commit=False)
            #print(donation)
            donation.user = request.user
            donation.save()
            messages.success(request,"Donatation request success")
            return redirect('home')
    else:
            form = DonationForm()
    return render(request,'donations/donation.html', {'form':form})

# def donation_view(request):
#     print(request.POST.get('purpose'))
#     if request.POST=="POST":
#         if request.POST['amount'] and request.POST['purpose']:
#             donation = Donation()
#             donation.amount = request.POST['amount']
#             donation.purpose = request.POST['purpose']
#             donation.user = request.user
#             donation.save()
#             print(request.POST['purpose'])
#             messages.success(request, "Donation request success")
#             return redirect('home')
#         else:
#             print('Maybe empty fields')
#     else:
#         print('Method Post error')
#     return render(request,'donations/donation.html',{})
