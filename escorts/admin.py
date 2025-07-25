from django.contrib import admin
from . models import Escort, Image, Town, County


@admin.register(Escort)
class EscortAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'escort_class', 'monthly_fee', 'renewal_date', 'status']

    def monthly_fee(self, obj):
        return obj.monthly_fee()
    
    def status(self, obj):
        return obj.status()

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display =['image_field', 'escort']


@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
    list_display =['id', 'name', 'county']


@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display =['id', 'name',]
    