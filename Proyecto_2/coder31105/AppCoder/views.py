from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.

def curso(request):
    curso=Curso(nombre="AWS", comision=3)
    curso1=Curso(nombre="Matematica", comision=1)
    curso2=Curso(nombre="Lengua", comision=2)
    curso.save()
    curso1.save()
    curso2.save()
    texto=f"Cursos Creados: nombre: {curso.nombre} comision:{curso.comision}"
    return HttpResponse(texto)
