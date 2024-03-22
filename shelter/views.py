from django.shortcuts import render, get_object_or_404
from .forms import PetForm
from .models import Pet
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
    else:
        form = PetForm()
    return render(request, 'create_pet.html', {'form': form})


def list_pets(request):
    pets = Pet.objects.all()
    return render(request, 'list_pets.html', {'pets': pets})


def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'pet_detail.html', {'pet': pet})

def contact(request):
    return render(request, 'contact.html')

def about_us(request):
    return render(request, 'about_us.html')
