from django.db import models

class TermsAndConditions(models.Model):
    name = models.CharField(max_length=50, default='terms and conditions')
    pdf_file = models.FileField(upload_to='terms/') 

    @property
    def pdf_url(self):
        return self.pdf_file.url
    
    