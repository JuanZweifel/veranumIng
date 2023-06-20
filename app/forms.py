from django import forms
from .models import Tipo_habitacion, Habitacion, Cliente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class frmAddTipo(forms.ModelForm):
    class Meta:
        model=Tipo_habitacion
        fields=["id_tipo_habitacion","nom_tipo","descrip_tipo","precio"]
        
class frmAddHabitacion(forms.ModelForm):
    
    class Meta:
        model = Habitacion
        fields = ["id_habitacion", "tipo_habitacion", "cant_camas", "cant_banos", "estado_habitacion", "hotel"]
        
class frmModifTipo(forms.ModelForm):
    class Meta:
        model=Tipo_habitacion
        fields=["nom_tipo","descrip_tipo","precio"]

class frmModifHabitacion(forms.ModelForm):
    class Meta:
        model=Habitacion
        fields = ["tipo_habitacion", "cant_camas", "cant_banos", "estado_habitacion", "hotel"]
        
        
class frmCrearCuenta(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1","password2"]
        
        
        
class frmPerfilCliente(forms.ModelForm):

    class Meta:
        model=Cliente
        fields=["run","dv","primer_nombre","segundo_nombre","apellido_paterno","apellido_materno","correo"]
        
        

class frmModifDatosCliente(forms.ModelForm):
    
    class Meta:
        model=Cliente
        fields=["run","dv","primer_nombre","segundo_nombre","apellido_paterno","apellido_materno","correo"]

class frmRecepcionista(forms.ModelForm):
    class Meta:
        model=Cliente
        fields = ["run"]