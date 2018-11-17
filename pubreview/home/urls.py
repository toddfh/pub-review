from django.contrib import admin
from django.urls import path, include
from accounts.views import register, login_view, \
    logout_view
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.login_test, name='login_test'),

]
