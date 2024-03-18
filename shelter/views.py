from django.shortcuts import render
from .forms import PetForm

# Create your views here.

def home_page(request):
    return render(request, 'home.html')

def create_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PetForm()
    return render(request, 'create_pet.html', {'form': form})