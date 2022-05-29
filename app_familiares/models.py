from django.db import models

class App_Familiares(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    fecha_nacimiento = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)
