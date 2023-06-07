from django import forms
from .models import Tipo_habitacion, Habitacion

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