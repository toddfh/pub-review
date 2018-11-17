from django.contrib import admin
from django.urls import path, include
from accounts.views import register, login_view, \
    logout_view

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/register/', register),
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', logout_view),
    path('pubs/', include('pubs.urls')),

]
