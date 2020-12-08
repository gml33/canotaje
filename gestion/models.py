from django.db import models
from django.conf import settings

class Curso(models.Model):
    fecha_inicio = models.DateField(auto_now_add=False, auto_now=False)
    fecha_finalizacion = models.DateField(auto_now_add=False, auto_now=False)
    contenido = models.TextField(blank=True)
    descripcion = models.TextField(blank=True)

class Alumno(models.Model):
    nombre = models.CharField(max_length=32)
    apellido = models.CharField(max_length=32)
    fecha_nac = models.DateField(auto_now_add=False, auto_now= False)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=64)
    observaciones = models.CharField(max_length=512, blank=True)
    curso = models.ManyToManyField(Curso)
    def __str__(self):
        return f'{self.nombre} {self.apellido}' 


class PadreAlumno(models.Model):
    alumno = models.ManyToManyField(Alumno, related_name='padre_alumno')
    nombre = models.CharField(max_length=32)
    apellido = models.CharField(max_length=32)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=64)
    def __str__(self):
        return f'{self.nombre} {self.apellido} Padre de :{self.alumno}'

class MadreAlumno(models.Model):
    alumno = models.ManyToManyField(Alumno, related_name='madre_alumno')
    nombre = models.CharField(max_length=32)
    apellido = models.CharField(max_length=32)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=64)
    def __str__(self):
        return f'{self.nombre} {self.apellido} Madre de :{self.alumno}'

class Pago(models.Model):
    Alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='nombre_instructor')
    fecha = models.DateField(auto_now_add=False, auto_now=False, blank=False)
    monto = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='pago_curso')
    def __str__(self):
        return f'monto: {self.monto}, fecha: {self.fecha}, alumno: {self.Alumno}'
