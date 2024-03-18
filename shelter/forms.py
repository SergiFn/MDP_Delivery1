from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'animal_type', 'age', 'weight', 'illness', 'breed']
