from django import forms
from .models import *

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

class PadreAlumnoForm(forms.ModelForm):
    class Meta:
        model = PadreAlumno
        fields = '__all__'

class MadreAlumnoForm(forms.ModelForm):
    class Meta:
        model = MadreAlumno
        fields = '__all__'

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = '__all__'

