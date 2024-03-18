from django.contrib import admin
from django.urls import path
from shelter.views import home_page


urlpatterns = [

    path('', home_page, name='home')
    
]