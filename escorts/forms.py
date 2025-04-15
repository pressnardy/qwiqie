from django import forms
from .models import Escort, Image, Service

class CreateEscortForm(forms.ModelForm):
    SKIN_COLORS = [
        ("dark skin", "darak_skin"), ("chocolate", "chocolate"), ("light skin", "light_skin"),
    ]
    BODY_TYPES = [
        ("petite", "petite"), ("medium", "medium"), ("curvy", "curvy")
        ]
    body_type = forms.ChoiceField(choices=BODY_TYPES, required=False)
    skin_color = forms.ChoiceField(choices=SKIN_COLORS, required=False)
    class Meta:
        model = Escort
        fields = ['name', 'gender', 'age', 'location', "escort_class", 'phone_number',
                   'skin_color', 'body_type', "created_by"
                     ]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-input", "id": "escort-name", 
                "placeholder": "name"}),
            "gender": forms.TextInput(attrs={"class": "form-input", "id": "gender"}),
            "age": forms.TextInput(attrs={"class": "form-input", "id": "age"}),
            "location": forms.TextInput(attrs={"class": "form-input", "id": "location"}),
            "phone_number": forms.TextInput(attrs={"class": "form-input", "id": "phone-number"}),
            "escort_class":  forms.TextInput(attrs={"class": "form-input", "id": "escort-class"}),
            "skin_color": forms.TextInput(attrs={"class": "form-input", "id": "skin-color"}),
            "body_type": forms.TextInput(attrs={"class": "form-input", "id": "body-type"}),
        }

    

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['escort_id', 'image']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["service_name", "price"]
        widgets = {
            "service_name": forms.TextInput(attrs={"class": "service", "placeholder": "Enter Service"}),
            "price": forms.TextInput(attrs={"class": "price", "placeholder": "Price in KES"})
        }


class EditEscortDetails(forms.ModelForm):
    class Meta:
        model = Escort
        fields = '__all__'
        


class EditService(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        

class RemoveServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = "__all__"


class RemoveImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"


def generate_attributes(fields: list):
    attributes = {}
    for field in fields:
        field_id = field.replace('_', '-') if '_' in field else field
        attributes[field] = {
            'class': 'form-input',
            'id': field_id
        }
    return attributes
