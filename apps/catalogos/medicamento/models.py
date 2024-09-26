from django.db import models
from apps.catalogos.presentacion.models import Presentacion
from apps.catalogos.unidad_medida.models import UnidadMedida
# Create your models here.
class Medicamento(models.Model):
    ID_Medicamento = models.AutoField(primary_key=True)
    Codigo_Medicamento = models.CharField(max_length=10, verbose_name='Codigo de medicamento', unique=True)
    Descripcion = models.CharField(max_length=200, verbose_name='Descripcion')
    Precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    ID_Presentacion = models.ForeignKey(Presentacion, verbose_name='Presentacion del medicamento', on_delete=models.PROTECT)
    ID_Unidad_Medida = models.ForeignKey(UnidadMedida, verbose_name='Unidad de medida', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Medicamento'

    def __str__(self):
        return f'{self.Codigo_Medicamento} - {self.Descripcion}'