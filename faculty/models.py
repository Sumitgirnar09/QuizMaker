from django.db import models
from zmq import NULL
from datetime import datetime

# Create your models here.

class Faculty(models.Model):
    GENDER_CHOICES = (
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Others"),
    )

    Teacher_id = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50,choices=GENDER_CHOICES,default=NULL)
    Dept = models.CharField(max_length=70, default="")
    Dob=models.DateField(default=datetime.now)
    pass1= models.CharField(max_length=70, default="")
    pass2= models.CharField(max_length=70, default="")
    email=models.EmailField(max_length=100 ,default="")
    
    
    def __str__(self):
        return self.First_Name+self.Last_Name
    
    
    