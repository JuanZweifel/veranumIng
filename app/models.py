from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.

validarletras = RegexValidator(r'^[a-zA-Z]*$', 'Ingrese solo letras')

class Tipo_habitacion(models.Model):
    id_tipo_habitacion=models.AutoField(primary_key=True, null=False)
    nom_tipo=models.CharField(max_length=50, null=False, unique=True, validators=[validarletras])
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
    DIGITOS_VERIFICADORES=[
        ("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),("8","8"),("9","9"),("0","0"),("K","K")
    ]
    
    
    usuario=models.OneToOneField(User, unique=True, related_name='perfil', on_delete=models.CASCADE)
    
    run=models.PositiveIntegerField(primary_key=True, null=False, validators=[MinValueValidator(1000000), MaxValueValidator(99999999)])  
    dv=models.CharField(null=False, max_length=1, choices=DIGITOS_VERIFICADORES) 
    primer_nombre=models.CharField(max_length=30, null=False, validators=[validarletras])
    segundo_nombre=models.CharField(max_length=30, null=False, validators=[validarletras])
    apellido_paterno=models.CharField(max_length=30, null=False, validators=[validarletras])
    apellido_materno=models.CharField(max_length=30, null=False, validators=[validarletras])
    correo=models.EmailField(max_length=254)

class Reserva(models.Model):
    id_reserva=models.AutoField(primary_key=True, null=False)
    fecha_reservacion=models.DateField(null=False)
    fecha_inicio=models.DateField(null=False)
    fecha_termino=models.DateField(null=False)
    total_reserva=models.PositiveIntegerField(null=False, validators=[MinValueValidator(1)])
    run_cliente=models.ForeignKey(Cliente, on_delete=models.PROTECT)
    #run_empleado=models.ForeignKey(, on_delete=models.PROTECT)
    