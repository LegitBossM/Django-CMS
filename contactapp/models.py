from django.db import models

# Create your models here.
class UserLogin(models.Model):
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    password = models.CharField(max_length=100)

class Contact(models.Model):
    userid = models.IntegerField()
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    relationship = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)