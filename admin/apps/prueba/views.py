from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.prueba.models import *

@login_required(login_url='/profiles/login')
def read_materia_view(request):
    materias=Materia.objects.all()
    context={
                'materias':materias,
            }
    return render(request, "prueba/readMateria.html",context)


def read_grado_view(request):
    grados=Grado.objects.all()
    context={
                'grados':grados,
            }
    return render(request, "prueba/readGrado.html",context)