from django.contrib import admin

from django.contrib.auth.admin import \
    UserAdmin as BaseUserAdmin

from .models import Pub


# class PubAdmin(BaseUserAdmin):
#     add_form = UserCreationForm

#     list_display = ('email', 'is_admin')
#     list_filter = ('is_admin',)

#     fieldsets = (
#                     (None, {'fields': ('email', 'password')}),
#                     ('Permissions',{'fields':('is_admin',)})
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()


admin.site.register(Pub)

