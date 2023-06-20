from django.contrib import admin
from app.models import Tipo_habitacion, Habitacion, Cliente, Reserva

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

class admReserva(admin.ModelAdmin):
    list_display=["id_reserva", "fecha_reservacion", "fecha_inicio", "fecha_termino", "total_reserva"]
    list_editables=["fecha_reservacion", "fecha_inicio", "fecha_termino", "total_reserva"]
        
    class Meta:
        model=Reserva

class admCliente(admin.ModelAdmin):
    list_display=["run", "primer_nombre", "segundo_nombre", "apellido_paterno", "apellido_materno", "correo"]
    list_editables=["primer_nombre", "segundo_nombre", "apellido_paterno", "apellido_materno", "correo"]

    class Meta:
        model=Cliente
    

admin.site.register(Tipo_habitacion, admTipo_habitacion)
admin.site.register(Habitacion, admHabitacion)
admin.site.register(Reserva, admReserva)
admin.site.register(Cliente, admCliente)
