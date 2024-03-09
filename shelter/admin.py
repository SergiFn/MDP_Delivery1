from django.contrib import admin
from .models import User, Worker, Customer, Pet, Adopt

# Register your models here.
admin.site.register(User)
admin.site.register(Worker)
admin.site.register(Customer)
admin.site.register(Pet)
admin.site.register(Adopt)