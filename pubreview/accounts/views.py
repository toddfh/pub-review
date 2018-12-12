from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import (
    UserCreationForm,
    UserLoginForm,
    UserUpdateForm,
    ProfileUpdateForm
)

from django.contrib.auth import login, logout, get_user_model

from .models import User


def home(request):
    return HttpResponse('Placeholder code')


def register(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f'Account Created!')
        return redirect('login')

    context = {
        'form': form
    }
    return render(request, "accounts/register.html",
                  context)


@login_required
def profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'accounts/profile.html', context)
