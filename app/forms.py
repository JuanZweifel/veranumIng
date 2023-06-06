from django import forms
from .models import Tipo_habitacion

class frmAddTipo(forms.ModelForm):
    class Meta:
        model=Tipo_habitacion
        fields=["id_tipo_habitacion","nom_tipo","descrip_tipo","precio"]
        
        
class frmModifTipo(forms.ModelForm):
    class Meta:
        model=Tipo_habitacion
        fields=["nom_tipo","descrip_tipo","precio"]