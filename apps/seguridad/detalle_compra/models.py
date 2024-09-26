from django.db import models
from apps.seguridad.compra.models import Compra
from apps.catalogos.medicamento.models import Medicamento
# Create your models here.
class DetalleCompra(models.Model):
    ID_DetalleCompra = models.AutoField(primary_key=True)
    Cantidad = models.IntegerField(verbose_name='Cantidad')
    Precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    ID_Compra = models.ForeignKey(Compra, verbose_name='Compra',on_delete=models.PROTECT)
    ID_Medicamento = models.ForeignKey(Medicamento, verbose_name='Medicamento',on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Detalles de Compra'