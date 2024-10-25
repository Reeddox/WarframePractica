from django.shortcuts import render, redirect
from WarframePracticaApp.models import WarframeCampos
from WarframePracticaApp.forms import WarframeForm

# Create your views here.

def Home(request):
    return render(request, 'index.html')

def WarframeListado(request):
    listado = WarframeCampos.objects.all()
    data = {'listado': listado}
    return render(request, 'ListadosWarframe.html', data)

def AgregarWarframe(request):
    form = WarframeForm()
    if request.method == 'POST':
        form = WarframeForm(request.POST)
        if form.is_valid():
            form.save()
        return Home(request)
    data = {'form' : form}
    return render(request, 'Formulario.html', data)

def EliminarWarframe(request, id):
    listado = WarframeCampos.objects.get(id = id)
    listado.delete()
    return redirect('../WarframeListado/')

def ModificarDatos(request, id):
    listado = WarframeCampos.objects.get(id = id)
    form = WarframeForm(instance = listado)
    if request.method == 'POST':
        form = WarframeForm(request.POST, instance = listado)
        if form.is_valid():
            form.save()
        return Home(request)
    data = {'form' : form}
    return render(request, 'Formulario.html', data)