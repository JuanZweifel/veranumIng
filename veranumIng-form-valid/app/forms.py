from django import forms
from .models import Tipo_habitacion, Habitacion
from django.core.validators import MinValueValidator

class frmAddTipo(forms.ModelForm):
    class Meta:
        model = Tipo_habitacion
        fields = ["nom_tipo", "descrip_tipo", "precio"]
        
class frmAddHabitacion(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ["tipo_habitacion", "cant_camas", "cant_banos", "estado_habitacion", "hotel"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cant_camas'].validators.append(MinValueValidator(1))
        self.fields['cant_banos'].validators.append(MinValueValidator(1))
