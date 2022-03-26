from django.db import models

# Create your models here.


class Pasajero(models.Model):

    nombre = models.CharField( max_length=50)
    apellido = models.CharField(max_length=50)
    pasaporte = models.CharField(primary_key=True,max_length=8)
    n_vuelo = models.IntegerField()

class Vuelo(models.Model):

    empresa = models.CharField(max_length=40)
    n_vuelo = models.IntegerField(primary_key=True)
    salida = models.DateField()

class Aeropuerto(models.Model):
    nombre= models.CharField(max_length=40)
    pais= models.CharField(max_length=40)
    

class Equipaje(models.Model):
    cantidad = models.IntegerField()
    nom_pasajero = models.CharField(max_length=120)


    