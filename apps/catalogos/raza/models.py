from django.db import models
from apps.catalogos.tipo_mascota.models import TipoMascota
# Create your models here.
class Raza(models.Model):
    ID_Raza = models.AutoField(primary_key=True)
    Codigo_Raza = models.CharField(max_length=10, verbose_name='Codigo de raza', unique=True)
    Descripcion = models.CharField(max_length=200, verbose_name='Descripcion')
    ID_TipoMascota = models.ForeignKey(TipoMascota, verbose_name='Tipo de Mascota', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Raza'

    def __str__(self):
        return f'{self.Codigo_Raza} {self.Descripcion}'