from django.db import models
from django.contrib.auth.models import *
from apps.states.models import *
from apps.prueba.models import *

# Create your models here.

class TipoDocumento(models.Model):

    nombre_documento=models.CharField(max_length=45, null=True)
    
    def __str__(self):
        return self.nombre_documento


class Estudiante(models.Model):
 
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, unique=True, default=1)
    tipo_documento=models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, null=True)
    numero_documento=models.CharField(max_length=45)
    estado = models.ForeignKey(Estado,  on_delete=models.CASCADE, null=True) 

class EstudiantePrueba():
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    prueba=models.ForeignKey(Prueba, on_delete=models.CASCADE, null=True)