from django import forms
from .models import Pet, Worker, Customer, Adopt


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'animal_type', 'age', 'weight', 'illness', 'breed']


class AdoptForm(forms.Form):
    pet = forms.ModelChoiceField(queryset=Pet.objects.all())
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
