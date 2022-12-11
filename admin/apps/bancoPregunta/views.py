# from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import HttpResponse
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, F
from django.db.models import Value as V
from django.db.models.functions import Concat
from django.contrib.auth.forms import AuthenticationForm
from apps.profiles.form import *
from apps.prueba.models import *
from apps.bancoPregunta.models import *
from apps.bancoPregunta.form import *


@login_required(login_url='/profiles/login')
def read_resultado_view(request):
    resultados=Resultado.objects.all()
    context={
                'resultados':resultados,
            }
    return render(request, "bancoPregunta/readResultados.html",context)

def create_pregunta_view(request):
    materias = Materia.objects.all()
    estados = Estado.objects.all()
    grados = Grado.objects.all()
    if request.method == 'POST': 
        form = PreguntaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()   
            return redirect('/bancoPregunta/readPregunta/')
        else:
            print(form.errors)
    else:
        form = PreguntaForm()
    context = {
        'form': form,
        'grados': grados,
        'estados': estados,
        'materias': materias,

    }
    return render (request,"bancoPregunta/createUpdatePregunta.html", context)


def update_pregunta_view(request,pk):
    pregunta = Pregunta.objects.get(id=pk)
    materias = Materia.objects.all()
    estados = Estado.objects.all()
    grados = Grado.objects.all()

    if request.method == 'POST':
        form = PreguntaForm(request.POST, request.FILES, instance = pregunta)
        if form.is_valid():
            form.save() 
            return redirect('/bancoPregunta/readPregunta/')
        else:
            print(form.errors)
    else:
        form = PreguntaForm()
    context = {
        'form': form,
        'grados': grados,
        'estados': estados,
        'materias': materias,
    }
    return render (request,"bancoPregunta/createUpdatePregunta.html", context)

def read_pregunta_view(request, pk=None):
    preguntas=Pregunta.objects.all()
    materias = Materia.objects.all()
    estados = Estado.objects.all()
    grados = Grado.objects.all()
    context = {
        'preguntas':preguntas
    }
    if pk: 
        pregunta = preguntas.get(id=pk)
        context['pregunta'] = pregunta
    if request.method == 'GET':
        if request.GET.get('action') =='search':
            if request.GET.get('materia_filter')!="":                    
                preguntas=preguntas.filter(Q(pregunta__materia__id=int(request.GET.get('materia_filter'))))
                if request.GET.get('grado_filter')!="":                    
                    preguntas=preguntas.filter(Q(pregunta__grado__id=int(request.GET.get('grado_filter'))))
                if request.GET.get('estado_filter')!="":
                    preguntas=preguntas.filter(Q(estado__id=int(request.GET.get('estado_filter'))))


        
    page = request.GET.get('page', 1)
    paginator = Paginator(preguntas,10)
    try:
        preguntas = paginator.page(page)
    except PageNotAnInteger:
        preguntas = paginator.page(1)
    except EmptyPage:
        preguntas = paginator.page(paginator.num_pages)

    context['preguntas'] = preguntas
    context['materias'] = materias
    context['estados'] = estados
    context['grados'] = grados

    return render (request,"bancoPregunta/readPregunta.html", context)


    
def read_respuestas_view(request, pk=None):
    respuestas=Respuesta.objects.all()
    context={
                'respuestas':respuestas,
            }

    if pk: 
        respuesta = respuestas.get(id=pk)
        context['respuesta'] = respuesta
        
    page = request.GET.get('page', 1)
    paginator = Paginator(respuestas,10)
    try:
        respuestas = paginator.page(page)
    except PageNotAnInteger:
        respuestas = paginator.page(1)
    except EmptyPage:
        respuestas = paginator.page(paginator.num_pages)
    
    context['respuestas'] = respuestas

    return render(request, "bancoPregunta/readRespuestas.html",context)