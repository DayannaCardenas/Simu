from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, F
from django.db.models import Value as V
from django.db.models.functions import Concat
from django.contrib.auth.forms import AuthenticationForm
from apps.profiles.form import *
from apps.prueba.models import *


def user_validate_group(roles=[]):
	def decorator(view_func):
		def arguments(request, *args, **kwargs):
			if request.user.groups.exists():
				if request.user.groups.all()[0].name in roles:
					return view_func(request, *args, **kwargs)
			return redirect('profiles:login')
		return arguments
	return decorator

def user_validate_group(roles=[]):
	def decorator(view_func):
		def arguments(request, *args, **kwargs):
			if request.user.groups.exists():
				if request.user.groups.all()[0].name in roles:
					return view_func(request, *args, **kwargs)
			return redirect('profiles:login')
		return arguments
	return decorator

def login_user(request):
    context={}
    if request.POST:
        form=AuthenticationForm(None, request.POST)
        username = request.POST['username']
        password = request.POST['password']
        if form.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profiles:home')
            else:
                form.add_error(None, "Usuario no encontrado")
        context['form']=form
    return render(request, "general/login.html", context)

def logout_user(request):
    logout(request)
    return redirect('/profiles/login')

@login_required(login_url='/profiles/login')
# @user_validate_group(roles=['Administrator', 'Authorizer'])
def home_view(request):
    return render(request, "general/home.html")

@login_required(login_url='/profiles/login')
def read_tipoDocumento_view(request):
    tipoDocumentos=TipoDocumento.objects.all()
    context={
                'tipoDocumentos':tipoDocumentos,
            }
    return render(request, "profiles/readTipoDocumento.html",context)

def create_estudiante_view(request):
    tipo_documentos = TipoDocumento.objects.all()
    grados = Grado.objects.all()
    if request.method == 'POST': 
        update_request = request.POST.copy()
        update_request.update({'email':request.POST['email'].lower(), 'username':request.POST['email'].lower(),})
        form = UserForm(update_request)
        form1 = EstudianteForm(update_request, request.FILES)
        if form.is_valid() and form1.is_valid():
            user = form.save(commit = False)
            user.set_password(form.data['new_password'])
            user.save()            
            estudiante = form1.save(commit = False)
            estudiante.user_id = user.id
            estudiante.save()
            return redirect('/profiles/readEstudiante/')   
        else:
            print(form.errors)
            print(form1.errors)
    else:
        form = UserForm()
        form1 = EstudianteForm()
    context = {
        'form': form,
        'form1': form1,
        'tipo_documentos': tipo_documentos,
        'grados': grados,
    }
    return render (request,"profiles/createUpdateEstudiante.html", context)

def update_estudiante_view(request,pk):
    estudiante = Estudiante.objects.get(user__id = pk)
    tipo_documentos = TipoDocumento.objects.all()
    if request.method == 'POST': 
        update_request = request.POST.copy()
        update_request.update({'user':estudiante.user.id})
        form = UserUpdateForm(update_request, instance = estudiante.user)
        form1 = EstudianteForm(update_request, request.FILES, instance = estudiante)
        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
            return redirect('/profiles/readEstudiante/')   
        else:
            print(form.errors)
            print(form1.errors)
    else:
        form = UserUpdateForm()
        form1 = EstudianteForm()
    context = {
        'form': form,
        'form1': form1,
        'tipo_documentos': tipo_documentos,
        'estudiante': estudiante,
    }
    return render (request,"profiles/createUpdateEstudiante.html", context)


def read_estudiante_view(request, pk=None):
    estudiantes = Estudiante.objects.all()
    context = {}
    if pk: 
        estudiante = estudiantes.get(user_id=pk)
        context['estudiante'] = estudiante

    page = request.GET.get('page', 1)
    paginator = Paginator(estudiantes,10)
    try:
        estudiantes = paginator.page(page)
    except PageNotAnInteger:
        estudiantes = paginator.page(1)
    except EmptyPage:
        estudiantes = paginator.page(paginator.num_pages)
    context['estudiantes'] = estudiantes

    return render (request,"profiles/readEstudiante.html", context)