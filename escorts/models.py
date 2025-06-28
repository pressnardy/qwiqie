from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils import timezone
import os
from dotenv import load_dotenv
from dateutil.relativedelta import relativedelta


load_dotenv()

class Escort(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, primary_key=True)
    skin_color = models.CharField(max_length=100, null=True, default=None, blank=True)
    body_type = models.CharField(max_length=100, null=True, default=None, blank=True)
    escort_class = models.CharField(max_length=100, null=True, default=None, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None, blank=True)
    
    @admin.display(description='status')
    def status(self):
        latest_payment = self.payments.order_by('-payment_id').first()
        subscription_status = 'Expired' if self.is_overdue() else 'Active'
        return subscription_status
        
    def renewal_date(self):
        latest_payment = self.payments.order_by('-payment_id').first()
        monthly_fee = self.monthly_fee()
        months_paid = latest_payment.amount // monthly_fee
        next_month_date = latest_payment.timestamp + relativedelta(months=months_paid)
        return next_month_date.date()

    def monthly_fee(self):
        payment_env_var = self.escort_class.upper() + "_MONTHLY_FEE"
        return int(os.getenv(payment_env_var))  

    def is_overdue(self):
        return timezone.now().date() > self.renewal_date()
    
    def __str__(self):
        return f"{self.name} | {self.gender} | {self.phone_number} | {self.status()} | {self.renewal_date()}"


class ProfilePicture(models.Model):
    image_id = models.AutoField(primary_key=True)
    escort_id = models.ForeignKey(Escort, on_delete=models.CASCADE, related_name='profile_picture')
    image_field = models.FileField(upload_to='profile_pics/', null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None, blank=True)


class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    escort_id = models.ForeignKey(Escort, on_delete=models.CASCADE, related_name='images')
    image_field = models.FileField(upload_to='images/', null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None, blank=True)
    
    
class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    escort_id = models.ForeignKey(Escort, on_delete=models.CASCADE, related_name='services')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None, blank=True)

    def __str__(self):
        return f"{self.service_name}, {self.price}"
    
 