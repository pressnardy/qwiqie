from django import forms


class PaymentForm(forms.Form):
    escort_phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(
        attrs={"class": "form-input mobile-phone", "id": "escort-phone", 'name': 'escort_phone'}
        ))
    payment_phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(
        attrs={"class": "form-input mobile-phone", 'id': "payment-phone", 'name':'payment_phone'}
        ))
    # account_reference = forms.CharField(max_length=12, widget=forms.TextInput(attrs={"class": "form-input", "id": "amount"}))
    amount = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.TextInput(
        attrs={"class": "form-input", "id": "amount", 'name': 'amount'}
        ))
    
    def __str__(self):
        return f"Escort_phone: {self.escort_phone}| Payment_phone: {self.payment_phone} | Amount: {self.amount}"
    