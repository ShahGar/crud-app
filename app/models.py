from django.db import models

# Create your models here.

class User(models.Model):
    GENDER_CHOICE =(
        ('M','Male'),
        ('F','Female'),
        ('O','Other')
    )
    full_name = models.CharField(max_length=25)
    address = models.CharField(max_length=122)
    contact = models.IntegerField()
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=8)
    
    def __str__(self):
        return f"{self.full_name} {self.address} {self.email} {self.contact}"