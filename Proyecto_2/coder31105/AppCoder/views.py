from django.shortcuts import render
from .models import Curso, Estudiante
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

def inicio(request):
    return render (request, "AppCoder/inicio.html")

def cursos(request):
    return render (request, "AppCoder/cursos.html")

def estudiantes(request):
    return render (request, "AppCoder/estudiantes.html")

def profesores(request):
    return render (request, "AppCoder/profesores.html")

def entregables(request):
    return render (request, "AppCoder/entregables.html")

def prueba(request):
    estudiante1=Estudiante(nombre="Aureliano", apellido="Buendia", email="aureb@ug.com")
    estudiante1.nombre="Cristina"
    estudiante1.save()




