from django.contrib import admin
from . models import Escort, Image


@admin.register(Escort)
class EscortAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'escort_class', 'monthly_fee', 'renewal_date', 'is_overdue']

    def monthly_fee(self, obj):
        return obj.monthly_fee()
    
    def is_overdue(self, obj):
        return obj.is_overdue()

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display =['image_field', 'escort']