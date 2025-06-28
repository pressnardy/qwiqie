from django.db import models
from django.utils import timezone
from datetime import datetime
from escorts.models import Escort

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    escort = models.ForeignKey(Escort, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=4000)
    timestamp = models.DateTimeField(default=timezone.now)
    account_reference = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return f"Payment: (Amount: {self.amount}, escort_id: {self.escort_id}, Date: {self.timestamp})"

    def escort_name(self):
        return self.escort.name
    
    