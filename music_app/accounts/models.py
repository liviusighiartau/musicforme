from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=56)
    address = models.CharField(max_length=50)
    age = models.IntegerField()
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.username
