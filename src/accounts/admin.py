from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_location','get_role','get_nid','get_bank')
    list_select_related = ('profile',)

    def get_nid(self, instance):
        return instance.profile.nid

    get_nid.short_description = 'NID'

    def get_bank(self, instance):
        return instance.profile.bank
    get_bank.short_description = 'Bank Account '

    def get_role(self, instance):
        return instance.profile.role

    get_role.short_description = 'Donation'

    def get_location(self, instance):
        return instance.profile.location

    get_location.short_description = 'Location'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)