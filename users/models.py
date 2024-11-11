
from django.db import models

# Create your models here.

class User(models.Model):
    
    your_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    grandfather_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    dob_gregorian = models.DateField(verbose_name="Date of Birth (Gregorian)", max_length=20)
    dob_ethiopian = models.DateField(verbose_name="Date of Birth (Ethiopian)",max_length=20)
    passport_number = models.CharField(max_length=20)
    passport_issue_date = models.DateField()
    passport_expiry_date = models.DateField()

    def __str__(self):
            return self.your_name

    