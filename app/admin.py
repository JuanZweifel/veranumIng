from django.contrib import admin
from app.models import Tipo_habitacion

# Register your models here.

class admTipo_habitacion(admin.ModelAdmin):
    list_display=["id_tipo_habitacion","nom_tipo","descrip_tipo", "precio"]
    list_editable=["nom_tipo","descrip_tipo", "precio"]

    class Meta:
        model=Tipo_habitacion

admin.site.register(Tipo_habitacion, admTipo_habitacion)