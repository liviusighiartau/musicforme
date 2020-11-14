from django.db import models

from accounts.models import CustomUser


class MusicalInstrument(models.Model):
    family = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    publish_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=50)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    musical_instrument = models.ForeignKey(MusicalInstrument, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title


class Messages(models.Model):
    pass

