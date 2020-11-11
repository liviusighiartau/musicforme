from django.db import models


class MusicalInstrument(models.Model):
    family = models.CharField(max_length=30)
    name = models.CharField(max_length=30)


class Ad(models.Model):
    pass


class Messages(models.Model):
    pass

