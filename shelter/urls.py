from django.urls import path, include
from shelter.views import home_page, create_pet, pet_detail, list_pets, contact, about_us, adopt_pet, list_adopted_pets

urlpatterns = [

    path('', home_page, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('create_pet/', create_pet, name='create_pet'),
    path('pet_detail/<int:pk>/', pet_detail, name='pet_detail'),
    path('list_pets/', list_pets, name='list_pets'),
    path('adopt_pet/', adopt_pet, name='adopt_pet'),
    path('adopt_list/', list_adopted_pets, name='list_adopted_pets'),
    path('contact/', contact, name='contact'),
    path('about-us/', about_us, name='about_us'),

]