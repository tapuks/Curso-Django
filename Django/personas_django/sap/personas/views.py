from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404

# Create your views here.
from personas.models import Persona


def detallePersona(request, id):
    # persona = Persona.objects.get(pk=id)
    # Si la url no existe sale el error 404
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalles.html', {'persona':persona})


personaForm = modelform_factory(Persona, exclude=[])

def nuevaPersona(request):
    formaPersona = personaForm()
    return render(request, 'personas/nueva.html', {'formaPersona':formaPersona})