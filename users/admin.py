from django.contrib import admin
from users.models import TermsAndConditions
# Register your models here.

admin.site.site_title = "Admin"
admin.site.site_header = "Qwiqee.com Admin"
admin.site.index_title = "Welcome to My Admin Portal"

@admin.register(TermsAndConditions)
class TermsAndConditionsAdmin(admin.ModelAdmin):
    list_display =['name', 'pdf_file']

