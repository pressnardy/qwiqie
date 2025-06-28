from django.contrib import admin
from .models import Payment


# Register your models here.

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'escort_name', 'amount', 'account_reference')

    def escort_name(self, obj):
        return obj.escort_name()
    