from django.db import models

# Create your models here.

class Medicamento(models.Model):
    nombreMarca = models.CharField(max_length=30)
    drogaComponente = models.CharField(max_length=30)
    laboratorio = models.CharField(max_length=30)
    codigoBarra = models.IntegerField()

class Laboratorio(models.Model):
    nombreLab = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    telefonoLab = models.IntegerField()

class Accion(models.Model):
    nombreAccion = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=80)
