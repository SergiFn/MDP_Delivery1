from django.contrib import admin
from django.urls import path, include
from shelter.views import home_page, create_pet, pet_detail, list_pets

urlpatterns = [

    path('', home_page, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('create_pet/', create_pet, name='create_pet'),
    path('pet_detail/<int:pk>/', pet_detail, name='pet_detail'),
    path('list_pets/', list_pets, name='list_pets'),
    #path('login/', login, name='login'),
    #path('password_reset/', password_reset, name='password_reset'),
    
]