from django.db import models

# Create your models here.


class Viajes(models.Model):
   
    destino = models.CharField( primary_key=True,max_length=100)
    pais = models.CharField(max_length=100)
    año = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.destino} - {self.pais} | {self. año}"
    

class Comidas(models.Model):

    nombre_comida = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100)
    opinion = models.IntegerField()

class Montanas(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    dificultad= models.IntegerField()

    




    