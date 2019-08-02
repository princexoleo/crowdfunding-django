from django.contrib import admin
from .models import Donation

# Register your models here.
class DonationAdmin(admin.ModelAdmin):
    model = Donation
    list_display =['user','purpose','amount','status']

admin.site.register(Donation,DonationAdmin)
