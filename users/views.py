from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from escorts.models import Escort
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from escorts import util
from django.db import IntegrityError
from django.http import HttpResponse

def in_testnet(request):
    return render(request, 'users/in_testnet.html')


@login_required
def account(request):
    user = request.user
    username = user.username
    if util.is_254_phone(username):
        user.username = f"0{username[-9:]}"
    escorts = Escort.objects.filter(created_by=request.user)
    context = {"user": user, "escorts": escorts}
    return render(request, 'users/account.html', context)


@login_required
def first_login(request, message):
    user = request.user
    message = message.replace(",", " ")
    escorts = Escort.objects.filter(created_by=request.user)
    context = {"user": user, "escorts": escorts, 'message':message}
    return render(request, 'users/account.html', context)


def register(request):
    message = 'Successful,registration.,Enjoy,your,free,trial,subscription'
    errors = []
    form = CustomAuthenticationForm()
    if request.method == 'POST':
        username = util.clean_phone(request.POST.get('username'))
        if User.objects.filter(username=username).exists():
            errors.append('Phone number already registered')
            return render(request, 'users/register.html', {'form': form, 'errors': errors})
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)  
                return redirect('users:first_login', message) 
            except IntegrityError:
                form.errors.add(None, 'invalid credentials')
        return render(request, 'users/register.html', {'form': form}) 
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form, 'errors': errors})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users:account')
        return render(request, 'users/login.html', {'form': form})
    form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    # messages.success(request, 'You have been successfully logged out.')
    return redirect('escorts:index')


def terms(request):
    return render(request, 'users/terms.html')
