from django.db import models

# Create your models here.

class familia(models.Model):

    nombre = models.CharField()
    apellido = models.CharField()
    edad = models.IntegerField()
    cumpleanios = models.DateField()
