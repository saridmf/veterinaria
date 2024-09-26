from django.db import models
from apps.catalogos.enfermedades.models import Enfermedades
from apps.catalogos.cita.models import Cita
# Create your models here.
class Detalle_Cita(models.Model):
    ID_DetalleCita = models.AutoField(primary_key=True)
    Codigo_DetalleCita = models.CharField(max_length=10, verbose_name='Codigo de detalle cita', unique=True)
    Descripcion = models.CharField(max_length=200, verbose_name='Descripcion')
    ID_Enfermedades = models.ForeignKey(Enfermedades, verbose_name='Enfermedad', on_delete=models.PROTECT)
    ID_Cita = models.ForeignKey(Cita, verbose_name='Cita No', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Detalles de Cita'