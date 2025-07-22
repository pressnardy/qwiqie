from django import forms
from .models import Escort, Image, Service, ProfilePicture

class CreateEscortForm(forms.ModelForm):
    SKIN_COLORS = [
        ("dark skin", "darak_skin"), ("chocolate", "chocolate"), ("light skin", "light_skin"),
    ]
    BODY_TYPES = [
        ("petite", "petite"), ("medium", "medium"), ("curvy", "curvy")
        ]
    GENDERS = [('female', 'female'), ('male', 'male')]
    CLASSES = [('vip', 'vip'), ('verified', 'verified'), ('general', 'general')]
    
    body_type = forms.ChoiceField(choices=BODY_TYPES, required=False)
    skin_color = forms.ChoiceField(choices=SKIN_COLORS, required=False)
    gender = forms.ChoiceField(choices=GENDERS, required=True)
    escort_class = forms.ChoiceField(choices=CLASSES, required=True)
    class Meta:
        model = Escort
        fields = ['name', 'gender', 'age', 'location', "escort_class", 'phone_number',
                   'skin_color', 'body_type', "created_by", 'bio', 'address',
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
            "address": forms.TextInput(attrs={"class": "form-input", "id": "address", 'placeholder': 'Address in format: County,Town,Area'}),
            "bio": forms.Textarea(attrs={
                "class": "text-area", "id": "bio", 'rows': 3, 'cols': 40,
                'placeholder': 'Type a short catchy description of yourself'
                }),
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image_field']
        widgets = {
            "image_field": forms.ClearableFileInput(attrs={"id": "upload-image", "type": "file"})
        }

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


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = ProfilePicture
        fields = "__all__"
        widgets = {
            "image_field": forms.ClearableFileInput(attrs={"id": "upload-image", "type": "file"})
        }


class FilterForm(forms.Form):
    BODY_TYPE_CHOICES = [
        ('petite', 'Petite'),
        ('medium', 'Medium'),
        ('curvy', 'Curvy'),
    ]

    AGE_CHOICES = [
        ('20-25', '20 - 25'),
        ('26-30', '26 - 30'),
        ('over 30', 'Over 30'),
    ]

    SKIN_COLOR_CHOICES = [
        ('dark', 'Dark Skin'),
        ('chocolate', 'Chocolate'),
        ('light-skin', 'Light Skin'),
    ]

    body_type = forms.ChoiceField(
        choices=BODY_TYPE_CHOICES, 
        widget=forms.RadioSelect
    )
    age = forms.ChoiceField(
        choices=AGE_CHOICES, 
        widget=forms.RadioSelect
    )
    skin_color = forms.ChoiceField(
        choices=SKIN_COLOR_CHOICES, 
        widget=forms.RadioSelect
    )
