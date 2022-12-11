from django.contrib import admin
from .models import Materia, Grado, Prueba, MateriaPrueba

# Register your models here.

admin.site.register(Materia)
admin.site.register(Grado)
admin.site.register(Prueba)
admin.site.register(MateriaPrueba)