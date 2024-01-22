from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=255)

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    contact = PhoneNumberField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    age = models.IntegerField()
    qualifications = models.TextField()
    description = models.TextField()