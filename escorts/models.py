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
        if value is None:
            return value
        if not isinstance(value, str):
            value = str(value)
        return value.lower()


class County(models.Model):
    id = models.AutoField(primary_key=True)
    name = LowercaseTextField(max_length=50, unique=True)
    
    @classmethod
    def get(cls, county_name):
        county_obj, created = cls.objects.get_or_create(name=county_name)
        return county_obj
    
    @classmethod
    def add_new(cls, county_name):
        county_obj, created = cls.objects.update_or_create(name=county_name)
        return county_obj

    @classmethod
    def get_towns_and_counties(cls):
        locations = {}
        counties = cls.objects.all()
        for county in counties:
            locations[county.name] = [town.name for town in county.towns.all()]
        return locations
    
    def towns(self):
        return self.towns.all()
    
    def escorts(self):
        return self.escorts.all()
    
    def __str__(self):
        return str(self.name)

class Town(models.Model):
    id = models.AutoField(primary_key=True)
    name = LowercaseTextField(max_length=50)
    county = models.ForeignKey(County, on_delete=models.CASCADE, null=True, default=None, related_name='towns')
    
    @classmethod
    def get_escorts(cls, town_name, county_name):
        town = cls.add(town_name=town_name, county_name=county_name)
        escorts = town.escorts.all()
        return escorts
    
    def escorts(self):
        return self.escorts.all()
    
    @classmethod
    def add_new(cls, town_name, county_name):
        county, created = County.objects.update_or_create(name=county_name)
        town, created = cls.objects.update_or_create(name=town_name, county=county)
        return created

    @classmethod
    def get(cls, town_name, county_name):
        county, created = County.objects.get_or_create(name=county_name)
        town, created = cls.objects.get_or_create(name=town_name, county=county)
        return town
    
    def __str__(self):
        return str(self.name)
    

class Escort(models.Model):
    name = LowercaseTextField(max_length=50)
    gender = LowercaseTextField(max_length=20)
    age = models.IntegerField()
    location = LowercaseTextField(max_length=50)
    address = LowercaseTextField(max_length=100, null=True, default=None, blank=False)
    phone_number = models.CharField(max_length=15, primary_key=True)
    skin_color = LowercaseTextField(max_length=100, null=True, default='chocolate', blank=False)
    body_type = LowercaseTextField(max_length=100, null=True, default='curvy', blank=True)
    escort_class = LowercaseTextField(max_length=100, null=True, default='vip', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='escorts')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    bio = models.TextField(max_length=110, null=True, blank=False, default=None)
    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name='escorts', null=True, default=None)
    town = models.ForeignKey(Town, on_delete=models.CASCADE, related_name='escorts', null=True, default=None)

    def save(self, *args, **kwargs):
        self.phone_number = util.clean_phone(self.phone_number)
        self.address = util.cleaned_address(self.address)
        address_dict = util.address_to_dict(self.address)
        self.county = County.get(county_name=address_dict['county'])
        self.town = Town.get(town_name=address_dict['town'], county_name=self.county.name)
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
        escort_monthly_fee = os.getenv(payment_env_var)
        if escort_monthly_fee and escort_monthly_fee.isdigit():
            return int(escort_monthly_fee)
        return None
    

    def is_overdue(self):
        if self.on_free_trial():
            return False
        if self.renewal_date():
            return timezone.now().date() > self.renewal_date()
        return True
    
    @classmethod
    def all_locations(cls):
        escorts = cls.objects.all()
        locations = {}
        for escort in escorts:
            address = util.address_to_dict(escort.address)
            town = address['town']
            county = address['county']
            if county not in  locations.keys():
                locations[county] = set()
            locations[county].add(town)
        return locations
    
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
    
