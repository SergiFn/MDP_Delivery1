from django.contrib import admin
from django.urls import path
from shelter.views import home_page, create_pet



urlpatterns = [

    path('', home_page, name='home'),
    path('create_pet/', create_pet, name='create_pet')
]