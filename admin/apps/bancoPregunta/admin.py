from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(BancoPregunta)
admin.site.register(PruebaBancoPregunta)
admin.site.register(Resultado)
admin.site.register(Retroalimentacion)
admin.site.register(Pregunta)
admin.site.register(Evaluacion)
admin.site.register(Respuesta)