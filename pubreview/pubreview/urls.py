from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import (
    register,
    profile_view,
)


urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),

    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),

    path('accounts/profile/', profile_view, name='profile'),
    path('pub/', include('pub.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
