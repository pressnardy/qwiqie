from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from escorts import util

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input', 'type': 'tel', 'required': "required",
        'id': 'username', "pattern": r"^(0\d{9})$", "placeholder":
        '0XXXXXXXXX'
        
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
        fields = ['username', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username = util.clean_phone(username)
        return username.lower() if username else username


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input', 'type': 'text', 'required': "required",
        'id': 'username', 'name': 'username',

    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'id': 'password', 'required': "required", 'name': 'password'
    }))
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username.lower() if username else username

