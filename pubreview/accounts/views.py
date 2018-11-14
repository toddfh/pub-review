from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.forms import RegistrationForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print('valid form!')
            form.save()
        return redirect('/')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)
