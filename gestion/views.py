from django.shortcuts import render, redirect, reverse
from .models import *
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib import messages
from django.conf import settings
from django.views.generic import TemplateView
from datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist
import operator

def index(request):
    if len(Alumno.objects.all()) > 0:
        data = Alumno.objects.all()
    else:
        data = None
    return render(request, 'gestion/index.html',{
        'data':data,
        'cantidad_alumnos':Alumno.objects.all().count(),
        'cantidad_cursos':Curso.objects.all().count(),
        'ultimo_curso':Curso.objects.last(),
        'alumnos_ultimo_curso':Alumno.objects.filter(curso = Curso.objects.last()).count(),
    })
#----------------------------Alumnos-----------------------------------------------------
def ver_alumnos(request):
    if len(Alumno.objects.all()) > 0:
        data = Alumno.objects.all()
    else:
        data = None
    return render(request, 'gestion/ver_alumno.html',{
        'data': data,
        })


def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        print(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            fecha_nac = form.cleaned_data['fecha_nac']
            edad = form.cleaned_data['edad']
            direccion = form.cleaned_data['direccion']
            observaciones = form.cleaned_data['observaciones']
            curso = form.cleaned_data['curso']
            form.save()
            messages.success(request, ('El Alumno fue cargado exitosamente.'))
            return HttpResponseRedirect(reverse('gestion:index'))                
        else:
            form = AlumnoForm()
    return render(request, 'gestion/agregar_alumno.html',{
        'cursos': Curso.objects.all(),
        })


def detalle_alumno(request, id):
    if len(PadreAlumno.objects.filter(alumno=id))>0:
        padre = PadreAlumno.objects.filter(alumno=id)
    else:
        padre = None
    if len(MadreAlumno.objects.filter(alumno=id))>0:
        madre = MadreAlumno.objects.filter(alumno=id)
    else:
        madre = None
    alumno = Alumno.objects.get(id=id)
    cursos = Curso.objects.filter(alumno=id)
    return render(request, 'gestion/detalle_alumno.html',{
        'cursos': cursos,
        'padre':padre,
        'madre':madre,
        'alumno':alumno,
        })
#----------------------------Cursos------------------------------------------------------
def ver_cursos(request):
    if len(Curso.objects.all()) > 0:
        data = Curso.objects.all()
    else:
        data = None
    return render(request, 'gestion/ver_curso.html',{
        'data': data,
        })

def agregar_curso(request):    
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('El Curso fue cargado exitosamente.'))
            return HttpResponseRedirect(reverse('gestion:index'))                
        else:
            form = CursoForm()
    return render(request, 'gestion/agregar_curso.html',{
        })
#----------------------------Pagos-------------------------------------------------------
'''
def ver_pagos(request):
    if len(Pago.objects.all()) > 0:
        data = Pago.objects.all()
    else:
        data = None
    return render(request, 'gestion/ver_pago.html',{
        'grupo': request.user.rol,
        'data': data,
        })

def agregar_curso(request):    
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_finalizacion = form.cleaned_data['fecha_finalizacion']
            contenido = form.cleaned_data['contenido']
            descripcion = form.cleaned_data['descripcion']
            form.save()
            messages.success(request, ('El Curso fue cargado exitosamente.'))
            return HttpResponseRedirect(reverse('gestion:index'))                
        else:
            form = AlumnoForm()
    return render(request, 'gestion/agregar_curso.html',{
        'grupo': request.user.rol,
        })
        '''