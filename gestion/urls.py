from django.urls import path
from . import views


app_name = 'gestion'


urlpatterns = [
    path('', views.index, name='index'),
    #------------------------Alumnos--------------------------------------------
    path('alumno/', views.ver_alumnos, name='ver_alumnos'),    
    path('alumno/detalle/<int:id>/', views.detalle_alumno, name='detalle_alumno'),
    #path('editar/alumno/<int:id>', views.editar_alumno, name='editar_alumno'),
    #path('alumno/<int:id>/eliminar', views.eliminar_alumno, name='eliminar_alumno'),    
    path('agregar/alumno/', views.agregar_alumno, name='agregar_alumno'),
    #------------------------Cursos------------------------------------------------------
    path('curso/', views.ver_cursos, name='ver_cursos'),
    path('agregar/curso/', views.agregar_curso, name='agregar_curso'),
    #path('editar/curso/<int:id>', views.editar_curso, name='editar_curso'),
    #path('curso/<int:id>/eliminar', views.eliminar_curso, name='eliminar_curso'),
    #------------------------Pago--------------------------------------------------------
    ]