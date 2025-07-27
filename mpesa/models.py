from django.db import models
from django.utils import timezone
from escorts.models import Escort

TILL = {'number': 3742126, 'store': 8181411, 'phone': 254769579848}

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    escort = models.ForeignKey(Escort, on_delete=models.SET_NULL, null=True, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=4000)
    transaction_date = models.IntegerField(null=True, blank=False)
    phone_number = models.CharField(max_length=12, null=True, blank=False)
    mpesa_receipt_number = models.CharField(max_length=50, null=True, blank=False)

    def escort_phone(self):
        ...

    def __str__(self):
        return f"Payment: (Amount: {self.amount}, escort_id: {self.escort.phone_number}, Date: {self.timestamp})"

    def escort_name(self):
        return self.escort.name
    

