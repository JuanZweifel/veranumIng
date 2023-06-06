from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .models import Tipo_habitacion
from .forms import frmAddTipo, frmModifTipo
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

def tipo_habitacion_modif(request,id):
    tipo_habitacion=get_object_or_404(Tipo_habitacion,id_tipo_habitacion=id)

    form = frmModifTipo(instance=tipo_habitacion)
    contexto={
        "form":form,
        "tipo_habitacion":tipo_habitacion
    }

    if request.method=="POST":

        form=frmModifTipo(data=request.POST,instance=tipo_habitacion)

        if form.is_valid():
            
            datos=form.cleaned_data
            mtipo=Tipo_habitacion.objects.get(id_tipo_habitacion=tipo_habitacion.id_tipo_habitacion)
            mtipo.nom_tipo=datos.get("nom_tipo")
            mtipo.descrip_tipo=datos.get("descrip_tipo")
            mtipo.precio=datos.get("precio")
            mtipo.save()
            return redirect(to="tipo_habitacion")

    return render(request,"app/tipo_habitacion_modificar.html",contexto)


def tipo_habitacion_eliminar(request,id):
    tipo_habitacion=get_object_or_404(Tipo_habitacion,id_tipo_habitacion=id)


    contexto={

        "tipo_habitacion":tipo_habitacion
    }

    if request.method=="POST":
        tipo_habitacion.delete()
        return redirect(to="tipo_habitacion")


    return render(request,"app/tipo_habitacion_delete.html",contexto)

