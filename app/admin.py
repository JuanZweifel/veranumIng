from django.contrib import admin
from app.models import Tipo_habitacion, Habitacion

# Register your models here.

class admTipo_habitacion(admin.ModelAdmin):
    list_display=["id_tipo_habitacion","nom_tipo","descrip_tipo", "precio"]
    list_editable=["nom_tipo","descrip_tipo", "precio"]

    class Meta:
        model=Tipo_habitacion
        
class admHabitacion(admin.ModelAdmin):
    list_display=["id_habitacion", "tipo_habitacion", "cant_camas", "cant_banos", "estado_habitacion", "hotel"]
    list_editables=["tipo_habitacion", "cant_camas", "cant_banos", "estado_habitacion", "hotel"]
    
    class Meta:
        model=Habitacion
    

admin.site.register(Tipo_habitacion, admTipo_habitacion)

admin.site.register(Habitacion, admHabitacion)