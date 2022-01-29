from django.db import models
from djongo import models
from phonenumber_field.modelfields import PhoneNumberField

class Employee(models.Model):
    _id = models.ObjectIdField()
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Gender = models.CharField(max_length=20)
    DOB = models.DateField(max_length=8)
    Salutation = models.TextField()
    Designation = models.CharField(max_length=20)
    Email = models.EmailField(max_length=254)
    Mobile = PhoneNumberField()
    AddressLine1 = models.TextField()
    AddressLine2 = models.TextField()
    City = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    Pin = models.IntegerField()
    Country = models.CharField(max_length=20)



    class Meta:
        abstract = False
        db_table = "Employee"
    
    def __str__(self):
        return f"{self.id}"
        