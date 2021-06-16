from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _


from core import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id'] #ordering in list
    list_display = ['email', 'firstName'] #displaying order in list
    fieldsets = (
        (None, {'fields': ('email', 'password')}), #Each bracket here is new section
        (_('Personal Info'), {'fields': ('firstName', 'lastName')}),
        (
            _('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)
