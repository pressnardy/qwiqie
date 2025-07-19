from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'id': 'phone-number',
        "name": "phone-number",

    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'id': 'username',
        
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'id': 'password1',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'id': 'password2',
    }))

    class Meta:
        model = User
        fields = ['username', 'phone_number', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username.lower() if username else username


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'id': 'username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'id': 'password',
    }))
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username.lower() if username else username

