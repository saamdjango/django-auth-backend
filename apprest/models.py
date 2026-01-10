from django.db import models

# Create your models here.
class Workers(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    dept = models.CharField(max_length=30)
    doj = models.DateField()

class Users(models.Model): 
    name = models.CharField(max_length= 40)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
