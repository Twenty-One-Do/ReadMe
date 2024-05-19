from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    gender_choices = (('Male', 'Male'), ('Female', 'Female'))
    name = models.CharField(max_length=10)
    gender = models.CharField(
        choices=gender_choices,
        max_length=10,
    )
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11)