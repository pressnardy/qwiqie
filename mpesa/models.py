from django.db import models
from escorts.models import Escort

# Create your models here.
 
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    escort_phone = models.CharField(max_length=15, null=True, blank=False)
    escort_id = models.ForeignKey(Escort, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False)
    timestamp = models.IntegerField(null=True, blank=False)
    account_reference = models.CharField(max_length=12, null=True, blank=False)

    def __str__(self):
        return f"Payment: (Amount: {self.amount}, escort_id: {self.escort_id}, Date: {self.timestamp})"

