from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import personas
from .forms import PersonaFrom
# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

def index(request):
    p = personas.objects.all()
    return render(request,'personas/index.html', {'p': p})

def formRegistro(request):
    formulario = PersonaFrom(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('index')
    return render(request,'personas/crear.html', {'formulario': formulario})

def formEditar(request, id):
    p = personas.objects.get(id=id)
    formulario = PersonaFrom(request.POST or None, request.FILES or None, instance=p)
    if formulario.is_valid() and request.method.POST:
        formulario.save()
        return redirect('index')
    return render(request,'personas/editar.html', {'formulario': formulario})

def borrarRegistro(request, id):
    p = personas.objects.get(id=id)
    p.delete()
    return redirect('index')