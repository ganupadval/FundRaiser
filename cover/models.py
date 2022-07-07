import email
from unicodedata import name
from django.db import models
from django.forms import CharField, ImageField, Textarea
from django.contrib.auth.models import User

# Create your models here.
class StartUp(models.Model):
    name = models.CharField(max_length=20)
    info = models.TextField()
    fund_req = models.IntegerField()
    fund_raised = models.IntegerField()
    products_sold = models.IntegerField()
    img = models.ImageField(upload_to='pics')
   
   
    
class Payments(models.Model):
    ammount =models.IntegerField(default=0)

class MedicalEm(models.Model):
    name = models.CharField(max_length=20)
    info = models.TextField()
    fund_req = models.IntegerField()
    fund_raised = models.IntegerField()
    img = models.ImageField(upload_to='pics')

class ContactUs(models.Model):
    name = models.TextField(max_length=20)
    email= models.EmailField()
    phone =models.BigIntegerField()
    msg = models.TextField()