from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe

from apps.account.models import User, Profile


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ('-date_joined', )
    list_display = ('username', 'first_name', 'last_name', 'date_joined', 'is_staff', )
    

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ordering = ('-user__date_joined', )
    list_display = ('c_email', 'c_name', 'birth_date', 'optin', )
    search_fields = ('user__email', 'user__first_name', 'user__last_name', )
    
    def c_email(self, obj):
        return obj.user.email
    c_email.short_description = _('E-mail')

    def c_name(self, obj):
        return mark_safe('<a href="/admin/dj_account/user/{}/change/">{}</a>'.format(obj.user.id, obj.user.get_full_name()))
    c_name.short_description = _('Name')

