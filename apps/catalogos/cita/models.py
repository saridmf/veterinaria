from django.db import models
from apps.catalogos.estado_de_cita.models import EstadodeCita
from apps.catalogos.mascota.models import Mascota
# Create your models here.
class Cita(models.Model):
    ID_Cita = models.AutoField(primary_key=True)
    Codigo_Cita = models.CharField(max_length=10, verbose_name='Codigo Cita', unique=True)
    Fecha_Realizacion = models.DateField(verbose_name='Fecha de realizacion')
    Fecha_de_Cita = models.DateField(verbose_name='Fecha para cita')
    Peso = models.CharField(max_length=30, verbose_name='Peso')
    ID_EstadoCita = models.ForeignKey(EstadodeCita, verbose_name='Estado de la cita',on_delete=models.PROTECT)
    ID_Mascota = models.ForeignKey(Mascota, verbose_name='Mascota',on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Cita'

    def __str__(self):
        return f'{self.Codigo_Cita} - {self.Fecha_Realizacion}'