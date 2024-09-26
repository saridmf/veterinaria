from django.db import models
from apps.catalogos.cita.models import Cita
from apps.catalogos.medicamento.models import Medicamento
# Create your models here.
class DetalleMedicamento(models.Model):
    ID_DetalleMedicamento = models.AutoField(primary_key=True)
    Cantidad = models.IntegerField(verbose_name='Cantidad')
    Descripcion = models.CharField(max_length=300, verbose_name='Descripcion')
    ID_Cita = models.ForeignKey(Cita, verbose_name='Cita No', on_delete=models.PROTECT)
    ID_Medicamento = models.ForeignKey(Medicamento, verbose_name='Medicamento', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Detalle Medicamento'