from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .models import Tipo_habitacion, Habitacion, Reserva
from django.http.response import JsonResponse
from .models import Tipo_habitacion, Habitacion, Cliente
from .forms import frmAddTipo, frmAddHabitacion
from .forms import frmAddTipo, frmModifTipo, frmModifHabitacion, frmRecepcionista
from .forms import frmCrearCuenta
from .forms import frmPerfilCliente, frmModifDatosCliente
from django.contrib.auth.models import User
# Create your views here.
def clientes(request):
    
    
    return render(request, "app/clientes.html")

def lista_clientes(_request):
    clientes = list(Cliente.objects.values())
    data={'clientes':clientes}
    return JsonResponse(data)


def modificar_perfil(request,id):
    modificar=get_object_or_404(Cliente,run=id)
    
    form = frmModifDatosCliente(instance=modificar)
    contexto={
        "form":form,
        "modificar":modificar
    }
    
    if request.method=="POST":
        
        form=frmModifDatosCliente(data=request.POST,instance=modificar)
        
        if form.is_valid():
            form.save()
            return redirect(to="clientes")

    return render(request,"app/modificar_cliente.html",contexto)


def crear_cuenta(request):
    formext=frmCrearCuenta(request.POST or None)
    formnormal=frmPerfilCliente(request.POST or None)

    contexto={
        "form":formext,
        "fuser":formnormal
        
    }

    if request.method=="POST":
        if formnormal.is_valid() and formext.is_valid():
            formext.save()
            datoext=formext.cleaned_data
            usr=User.objects.get(username=datoext.get("username"))
            u=Cliente()
            datos=formnormal.cleaned_data
            u.run=datos.get("run") 
            u.dv=datos.get("dv")
            u.primer_nombre=datos.get("primer_nombre")
            u.segundo_nombre=datos.get("segundo_nombre")
            u.apellido_paterno=datos.get("apellido_paterno")
            u.apellido_materno=datos.get("apellido_materno")
            u.correo=datos.get("correo")
            u.usuario=usr
            u.save()
        
    return render(request,"app/registration/crear_cuenta.html",contexto)

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
    tipo_habi=get_object_or_404(Tipo_habitacion,id_tipo_habitacion=id)
    try:
        habi=Habitacion.objects.filter(tipo_habitacion=tipo_habi)
    except:
        habi=None

    contexto={

        "tipo_habitacion":tipo_habi,
        "habi":habi
    }

    if request.method=="POST":
        tipo_habi.delete()
        return redirect(to="tipo_habitacion")


    return render(request,"app/tipo_habitacion_delete.html",contexto)

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

            return HttpResponseRedirect("habitacion")

    else:
        form = frmAddHabitacion()

    return render(request, "app/habitacion_add.html", {"form": form})


def index(request):
    return render(request, 'app/index.html')


def index_usuario(request):
    return render(request, 'app/index_usuario.html')


def habitacion_eliminar(request,id):
    habi=get_object_or_404(Habitacion,id_habitacion=id)
    contexto={
        "habi":habi,
    }

    if request.method=="POST":
        habi.delete()
        return redirect(to="habitacion")

    return render(request,"app/habitacion_delete.html",contexto)

def habitacion_modif(request,id):
    habi=get_object_or_404(Habitacion,id_habitacion=id)
    form = frmModifHabitacion(instance=habi)
    contexto={
        "form":form,
        "habi":habi
    }
    if request.method=="POST":
        form=frmModifHabitacion(data=request.POST,instance=habi)
        if form.is_valid():
            form.save()
            return redirect(to="habitacion")
    return render(request,"app/habitacion_modificar.html",contexto)

def verificarReserva(request):
    if request.method == "POST":
        form = frmRecepcionista(request.POST)
        rut = form.data['run']
        return redirect('recepcionista', id=rut)
    else:
        form = frmRecepcionista()
        context = {
            "form":form
        }
        return render(request,"app/verificarReserva.html",context)

def recepcionista(request, id):
    reserva = Reserva.objects.filter(run_cliente=id)
    context = {
        "reserva":reserva
    }
    return render(request, "app/recepcionista.html",context)