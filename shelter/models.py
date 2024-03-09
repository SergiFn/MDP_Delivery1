from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15)
    dni = models.CharField(max_length=15, primary_key=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Worker(User):
    salary = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Customer(User):
    economic_status = models.CharField(max_length=100)
    housing_type = models.CharField(max_length=100)


class Pet(models.Model):
    name = models.CharField(max_length=100)
    animal_type = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.CharField(max_length=100)
    illness = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return self.name


class Adopt(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.pet.name
