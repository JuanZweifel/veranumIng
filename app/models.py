from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Tipo_habitacion(models.Model):
    id_tipo_habitacion=models.AutoField(primary_key=True, null=False)
    nom_tipo=models.CharField(max_length=50, null=False)
    descrip_tipo=models.TextField(null=True)
    precio=models.PositiveIntegerField(null=False,  validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.nom_tipo}"
    
class Habitacion(models.Model):
    ESTADO_HABITACIONES= [
    ("D", "Disponible"),
    ("ND", "No disponible"),
    ]
    
    HOTELES= [
    ("H1", "Hotel 1"),
    ("H2", "Hotel 2"),
    ]
    
    id_habitacion=models.PositiveIntegerField(primary_key=True, null=False)
    tipo_habitacion=models.ForeignKey(Tipo_habitacion, on_delete=models.PROTECT)
    cant_camas=models.PositiveIntegerField(null=False, default=0, validators=[MinValueValidator(1), MaxValueValidator(4)])
    cant_banos=models.PositiveIntegerField(null=False, default=0, validators=[MinValueValidator(1), MaxValueValidator(3)])
    estado_habitacion=models.CharField(null=False, max_length=15, choices=ESTADO_HABITACIONES)
    hotel=models.CharField(null=False,max_length=15, choices=HOTELES)

class Reserva(models.Model):
    id_reserva=models.AutoField(primary_key=True, null=False)
    fecha_reservacion=models.DateField(null=False)
    fecha_inicio=models.DateField(null=False)
    fecha_termino=models.DateField(null=False)
    total_reserva=models.PositiveIntegerField(null=False, validators=[MinValueValidator(1)])