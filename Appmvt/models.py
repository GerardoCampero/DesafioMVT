from django.db import models

# Create your models here.


class Familiares(models.Model):

    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha = models.DateField()