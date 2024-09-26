from django.db import models
from apps.catalogos.raza.models import Raza
from apps.seguridad.cliente.models import Cliente

# Create your models here.
class Mascota(models.Model):
    ID_Mascota = models.AutoField(primary_key=True)
    Codigo_Mascota = models.CharField(max_length=10, verbose_name='Codigo de mascota', unique=True)
    Descripcion = models.CharField(max_length=200, verbose_name='Descripcion')
    Nombre_Mascota = models.CharField(max_length=20, verbose_name='Nombre de mascota')
    ID_Raza = models.ForeignKey(Raza, verbose_name='Raza', on_delete=models.PROTECT)
    ID_Cliente = models.ForeignKey(Cliente, verbose_name='Cliente', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Mascota'

    def __str__(self):
        return f'{self.Codigo_Mascota} - {self.Nombre_Mascota}'