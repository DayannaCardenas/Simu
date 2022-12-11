from django.db import models
from django.contrib.auth.models import *
from apps.bancoPregunta.models import *
from apps.states.models import *

class Materia(models.Model):
    
    nombre_materia=models.CharField(max_length=45, null=True, blank=True)
    estado=models.ForeignKey(Estado, blank=True, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.nombre_materia 


class Grado(models.Model):
        
    nombre_grado=models.CharField(max_length=45, null=True)
    
    def __str__(self):
        return self.nombre_grado   


class Prueba(models.Model):
    
    nombre=models.CharField(max_length=45, null=True, blank=True)
    fecha_aplicacion=models.DateTimeField()
    resultado=models.ForeignKey('bancoPregunta.Resultado', blank=True, on_delete=models.CASCADE, null=True)
    grado=models.ForeignKey(Grado, blank=True, on_delete=models.CASCADE, null=True)
    estado=models.ForeignKey(Estado, blank=True, on_delete=models.CASCADE, null=True)
    
    materia = models.ManyToManyField(
        Materia,
    )
    
    prueba_banco=models.ManyToManyField(
        BancoPregunta,
    )
    
    def __str__(self):
        return self.nombre  

    
class MateriaPrueba(models.Model):  
    
    materia=models.ForeignKey(Materia, blank=True, on_delete=models.CASCADE, null=True)
    prueba=models.ForeignKey(Prueba, blank=True, on_delete=models.CASCADE, null=True)