
from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    grandfather_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)


def __str__(self):
        return self.username