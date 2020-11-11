from django.contrib.auth.models import User
from django.db import models


class CustomUser(User):
    # name = User.CharField(max_length=60)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=56)
    address = models.CharField(max_length=50)
    age = models.IntegerField()


class Teacher(models.Model):
    pass
    # name
    # city
    # country
    # address
    # phone number

