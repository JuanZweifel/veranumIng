from django.db import models

# Create your models here.
class Tipo_habitacion(models.Model):
    id_tipo_habitacion=models.AutoField(primary_key=True, null=False)
    nom_tipo=models.CharField(max_length=50, null=False)
    descrip_tipo=models.TextField(null=True)