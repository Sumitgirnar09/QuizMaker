from ast import Pass
from asyncio.windows_events import NULL
from email.policy import default
from django.db import models

# Create your models here.

class Administrator(models.Model):
    
    Name=models.CharField(max_length=200,default=NULL)
    Username=models.CharField(max_length=200,default=NULL)
    Email=models.EmailField(max_length=200)
    Pass=models.CharField(max_length=200)
    
    
    
    