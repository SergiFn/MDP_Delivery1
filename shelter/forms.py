from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Pet, Worker, Customer, Adopt


class PetForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    animal_type = forms.ChoiceField(choices=Pet.ANIMAL_TYPE)
    age = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)])
    weight = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)])
    illness = forms.ChoiceField(choices=Pet.ILLNESS_CHOICES)
    breed = forms.CharField(max_length=100)

    class Meta:
        model = Pet
        fields = ['name', 'animal_type', 'age', 'weight', 'illness', 'breed']


class AdoptForm(forms.Form):
    pet = forms.ModelChoiceField(queryset=Pet.objects.filter(is_adopted=False))
    date = forms.DateField(input_formats=['%d/%m/%Y'])
    worker = forms.ModelChoiceField(queryset=Worker.objects.all())
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())

    class Meta:
        model = Adopt
        fields = ['pet', 'date', 'worker', 'customer']

    def save(self):
        data = self.cleaned_data
        adopt = Adopt.objects.create(pet=data['pet'], date=data['date'], worker=data['worker'], customer=data['customer'])
        adopt.save()
        return adopt
