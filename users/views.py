from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from escorts.models import Escort
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def account(request):
    user = request.user
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
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('users:first_login', message)  
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('users:account')
            else:
                message = ('Invalid username or password.')
                form = CustomAuthenticationForm()
                return render(request, 'users/login.html', {'form': form, "message": message})  
   
    form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    # messages.success(request, 'You have been successfully logged out.')
    return redirect('escorts:index')



