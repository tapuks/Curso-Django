from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from personas.models import Persona


def bienvenido(request):

    return render(request, "bienvenido.html",{'msg1': 'Valor mensaje 1', 'msg2': 'Valor mensaje 2'})


def adios(request):
    return HttpResponse("adios")


def saludo(request):
    return HttpResponse("huolaaa")

def contacto(request):
    return HttpResponse("cp: 22549 \n tel: 652200331")

def inicio(request):
    num_personas = Persona.objects.count()
    personas = Persona.objects.all()
    return render(request, "inicio.html", {'num_personas': num_personas, 'personas': personas})
