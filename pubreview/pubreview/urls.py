from django.contrib import admin
from django.urls import path
from accounts.views import register, login_view, \
    logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/register/', register),
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', logout_view),

]
