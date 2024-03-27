from django.shortcuts import render, get_object_or_404
from .forms import PetForm, AdoptForm
from .models import Pet, Adopt
from django.contrib.auth.decorators import login_required


# Create your views here.

def home_page(request):
    return render(request, 'home.html')


@login_required
def create_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmations/confirmation_create_pet.html')

    else:
        form = PetForm()
    return render(request, 'create_pet.html', {'form': form})


def list_pets(request):
    pets = Pet.objects.all()
    return render(request, 'list_pets.html', {'pets': pets})


def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'pet_detail.html', {'pet': pet})


@login_required
def adopt_pet(request):
    if request.method == 'POST':
        form = AdoptForm(request.POST)
        if form.is_valid():
            adoption = form.save()
            pet = adoption.pet
            pet.is_adopted = True
            pet.save()
            return render(request, 'confirmations/confirmation_adopt_pet.html')

    else:
        form = AdoptForm()
    return render(request, 'adopt_pet.html', {'form': form})


def list_adopted_pets(request):
    adopts = Adopt.objects.all()
    return render(request, 'list_adopted_pets.html', {'adopts': adopts})


def contact(request):
    if request.method == 'POST':
        return render(request, 'confirmations/thanks_contact.html')

    return render(request, 'contact.html')


def about_us(request):
    return render(request, 'about_us.html')
