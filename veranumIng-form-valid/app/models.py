from django.db import models

# Create your models here.
class Tipo_habitacion(models.Model):
    id_tipo_habitacion=models.AutoField(primary_key=True, null=False)
    nom_tipo=models.CharField(max_length=50, null=False)
    descrip_tipo=models.TextField(null=True)
    precio=models.IntegerField(null=False)

    def __str__(self):
        return f"{self.nom_tipo}"
    
class Habitacion(models.Model):
    ESTADO_HABITACIONES= [
    ("DS", "Disponible"),
    ("ND", "No_disponible"),
    ]
    
    id_habitacion=models.IntegerField(primary_key=True, null=False)
    tipo_habitacion=models.ForeignKey(Tipo_habitacion, on_delete=models.PROTECT)
    cant_camas=models.IntegerField(null=False, default=0)
    cant_banos=models.IntegerField(null=False, default=0)
    estado_habitacion=models.CharField(null=False, max_length=15, choices=ESTADO_HABITACIONES)
    hotel=models.IntegerField(null=False)