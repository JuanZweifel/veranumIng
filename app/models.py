from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.

validarletras = RegexValidator(r'^[a-zA-ZñÑ]*$', 'Ingrese solo letras')

class Tipo_habitacion(models.Model):
    id_tipo_habitacion=models.AutoField(primary_key=True, null=False)
    nom_tipo=models.CharField(max_length=50, null=False, unique=True)
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
    
    id_habitacion=models.PositiveIntegerField(primary_key=True, null=False, unique=True)
    tipo_habitacion=models.ForeignKey(Tipo_habitacion, on_delete=models.PROTECT)
    cant_camas=models.PositiveIntegerField(null=False, default=0, validators=[MinValueValidator(1), MaxValueValidator(4)])
    cant_banos=models.PositiveIntegerField(null=False, default=0, validators=[MinValueValidator(1), MaxValueValidator(3)])
    estado_habitacion=models.CharField(null=False, max_length=15, choices=ESTADO_HABITACIONES)
    hotel=models.CharField(null=False,max_length=15, choices=HOTELES)
    
class Cliente(models.Model):
    
    usuario=models.OneToOneField(User, unique=True, related_name='perfil', on_delete=models.CASCADE)
    
    run=models.CharField(primary_key=True, null=False, max_length=10)   
    primer_nombre=models.CharField(max_length=30, null=False, validators=[validarletras])
    segundo_nombre=models.CharField(max_length=30, null=False, validators=[validarletras])
    apellido_paterno=models.CharField(max_length=30, null=False, validators=[validarletras])
    apellido_materno=models.CharField(max_length=30, null=False, validators=[validarletras])
    correo=models.EmailField(max_length=254, unique=True)

class Reserva(models.Model):
    id_reserva=models.AutoField(primary_key=True, null=False)
    fecha_reservacion=models.DateField(null=False)
    fecha_inicio=models.DateField(null=False)
    fecha_termino=models.DateField(null=False)
    total_reserva=models.PositiveIntegerField(null=False, validators=[MinValueValidator(1)])
    run_cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion=models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    #run_empleado=models.ForeignKey(, on_delete=models.PROTECT)
    