from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q, F
from apps.prueba.models import *
import random


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

def read_prueba_view(request, pk=None):
    preguntas=Pregunta.objects.all()
    preguntas2=Pregunta.objects.all()
    # materias = Materia.objects.all()
    # estados = Estado.objects.all()
    # grados = Grado.objects.all()
    context = {
        'preguntas':preguntas
    }
    if pk: 
        pregunta = preguntas.get(id=pk)
        context['pregunta'] = pregunta
    
    preguntas=preguntas.filter()
    
    preguntas=preguntas.filter(Q(grado__id=int(1)))
    preguntasEspanol=preguntas.filter(Q(materia__id=int(2)))
    preguntasMatematicas=preguntas.filter(Q(materia__id=int(1)))
    

    print(type(preguntas))
    preguntasEspanol = random.choices(preguntasEspanol, weights=None,  cum_weights=None, k = 2)
    preguntasMatematicas = random.choices(preguntasMatematicas, weights=None,  cum_weights=None, k = 2)

    # page = request.GET.get('page', 1)
    # paginator = Paginator(preguntas,10)
    # try:
    #     preguntas = paginator.page(page)
    # except PageNotAnInteger:
    #     preguntas = paginator.page(1)
    # except EmptyPage:
    #     preguntas = paginator.page(paginator.num_pages)

    context['preguntasEspanol'] = preguntasEspanol
    context['preguntasMatematicas'] = preguntasMatematicas
    # context['materias'] = materias
    # context['estados'] = estados
    # context['grados'] = grados

    return render (request,"prueba/readPrueba.html", context)
