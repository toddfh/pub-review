from django.contrib import admin

from django.contrib.auth.models import Group
from django.contrib.auth.admin import \
    UserAdmin as BaseUserAdmin

from .forms import UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm

    list_display = ('email', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
                    (None, {'fields': ('email', 'password')}),
                    ('Permissions',{'fields':('is_admin',)})
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

admin.site.unregister(Group)
