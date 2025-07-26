from django.contrib import admin
from .models import Payment


# Register your models here.

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'phone_number', 'amount', 'mpesa_receipt_number')

    def escort_phone(self, obj):
        return obj.phone_number
    