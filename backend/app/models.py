from django.db import models

class Hermana(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    fechadenacimiento = models.DateField()

class Prima(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    fechadenacimiento = models.DateField()

class Tia(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    fechadenacimiento = models.DateField()
