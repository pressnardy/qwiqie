from django import forms
from .models import Payment


class PaymentForm(forms.Form):
    escort_phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={"class": "form-input", "id": "escort-phone"}))
    # account_reference = forms.CharField(max_length=12, widget=forms.TextInput(attrs={"class": "form-input", "id": "amount"}))
    amount = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={"class": "form-input", "id": "amount"}))
