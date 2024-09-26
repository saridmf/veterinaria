from django.db import models
from apps.seguridad.cliente.models import Cliente
# Create your models here.
class Venta(models.Model):
    ID_Venta = models.AutoField(primary_key=True)
    Codigo_Venta = models.CharField(max_length=10, verbose_name='Codigo de venta', unique=True)
    Descripcion = models.CharField(max_length=200, verbose_name='Descripcion')
    Fecha = models.DateField(verbose_name='Fecha')
    ID_Cliente = models.ForeignKey(Cliente, verbose_name='Nombre del cliente', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Venta'

    def __str__(self):
        return f'{self.Codigo_Venta} - {self.Fecha}'