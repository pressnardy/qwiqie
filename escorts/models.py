from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils import timezone
import os
from dotenv import load_dotenv
from dateutil.relativedelta import relativedelta
from escorts import util

load_dotenv()

class LowercaseTextField(models.CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname)
        return value.lower() if value else value
  

class Escort(models.Model):
    name = LowercaseTextField(max_length=50)
    gender = LowercaseTextField(max_length=20)
    age = models.IntegerField()
    location = LowercaseTextField(max_length=50)
    phone_number = models.CharField(max_length=15, primary_key=True)
    skin_color = LowercaseTextField(max_length=100, null=True, default='chocolate', blank=True)
    body_type = LowercaseTextField(max_length=100, null=True, default='curvy', blank=True)
    escort_class = LowercaseTextField(max_length=100, null=True, default='vip', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    bio = models.TextField(max_length=110, null=True, blank=False, default=None)

    def save(self, *args, **kwargs):
        self.phone_number = util.clean_phone(self.phone_number)
        super().save(*args, **kwargs)

    def on_free_trial(self):
        if not self.date_created:
            return False
        free_trial_end_date = self.date_created + relativedelta(months=1)
        return timezone.now().date() <= free_trial_end_date.date()

    @admin.display(description='status')
    def status(self):
        subscription_status = 'Expired' if self.is_overdue() else 'Active'
        return subscription_status
        
    def renewal_date(self):
        if latest_payment := self.payments.order_by('-payment_id').first():
            monthly_fee = self.monthly_fee()
            if not monthly_fee:
                return None
            months_paid = latest_payment.amount // monthly_fee
            if self.on_free_trial():
                months_paid = latest_payment.amount // monthly_fee + 1
        
            next_payment_date = latest_payment.timestamp + relativedelta(months=months_paid)
            return next_payment_date.date()
        return None

    def monthly_fee(self):
        escort_class = self.escort_class
        if not escort_class:
            escort_class = 'vip'
        payment_env_var = str(self.escort_class).upper() + "_MONTHLY_FEE"
        if payment_env_var:
            escort_monthly_fee = int(os.getenv(payment_env_var)) 
        return escort_monthly_fee or None


    def is_overdue(self):
        if self.on_free_trial():
            return False
        if self.renewal_date():
            return timezone.now().date() > self.renewal_date()
        return True
    
    def __str__(self):
        return f"{self.name} | {self.gender} | {self.phone_number} | {self.status()} | {self.renewal_date()}"


class ProfilePicture(models.Model):
    image_id = models.AutoField(primary_key=True)
    escort_id = models.ForeignKey(Escort, on_delete=models.CASCADE, related_name='profile_picture')
    image_field = models.FileField(upload_to='profile_pics/', null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None, blank=True)


class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    escort = models.ForeignKey(Escort, on_delete=models.CASCADE, related_name='images')
    image_field = models.FileField(upload_to='images/', null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None, blank=True)
    
    
class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = LowercaseTextField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    escort = models.ForeignKey(Escort, on_delete=models.CASCADE, related_name='services')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None, blank=True)

    def __str__(self):
        return f"{self.service_name}, {self.price}"
    
