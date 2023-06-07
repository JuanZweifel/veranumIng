from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Tipo_habitacion, Habitacion
from .forms import frmAddTipo, frmAddHabitacion
# Create your views here.

def tipo_habitacion(request):
    tipo = Tipo_habitacion.objects.all()
    context = {
        "tipo":tipo
    }
    return render(request, 'app/tipo_habitacion.html', context)

def tipo_habitacion_add(request):
    if request.method == "POST":
        form = frmAddTipo(request.POST)
        if form.is_valid():
            # PREGUNTAR PROFE si es necesario limpiar la informacion 
            # cuando el formulario se hace desde la base de datos
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('tipo_habitacion')
    else:
        form = frmAddTipo()
    context = {
        "form":form
    }
    return render(request, 'app/tipo_habitacion_add.html', context)

def habitacion(request):
    habitaciones = Habitacion.objects.all()
    
    context = {
        "habitaciones":habitaciones
    }
    
    return render(request, "app/habitacion.html", context)

def habitacion_add(request):
    if request.method == "POST":
        form = frmAddHabitacion(request.POST)
        if form.is_valid():

            form.save()

            return HttpResponseRedirect("habitacion_add")

    else:
        form = frmAddHabitacion()

    return render(request, "app/habitacion_add.html", {"form": form})