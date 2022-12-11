from django.db import models

# Create your models here.

class Estado(models.Model):
    
    nombre_estado=models.CharField(max_length=45)
    
    def __str__(self):
        return self.nombre_estado
    