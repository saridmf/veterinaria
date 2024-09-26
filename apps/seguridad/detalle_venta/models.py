from django.db import models
from apps.seguridad.venta.models import Venta
from apps.catalogos.medicamento.models import Medicamento
# Create your models here.
class DetalleVenta(models.Model):
    ID_DetalleVenta = models.AutoField(primary_key=True)
    Cantidad = models.IntegerField(verbose_name='Cantidad')
    Precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    ID_Venta = models.ForeignKey(Venta, verbose_name='Venta', on_delete=models.PROTECT)
    ID_Medicamento = models.ForeignKey(Medicamento, verbose_name='Medicamento', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Detalles de venta'