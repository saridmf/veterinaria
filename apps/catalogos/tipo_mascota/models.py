from django.db import models

# Create your models here.
class TipoMascota(models.Model):
    ID_TipoMascota = models.AutoField(primary_key=True)
    Codigo_TipoMascota = models.CharField(max_length=10, verbose_name='Codigo de tipo mascota', unique=True)
    Descripcion = models.CharField(max_length=200, verbose_name='Direccion')

    class Meta:
        verbose_name = 'Tipo de mascota'

    def __str__(self):
        return f'{self.Codigo_TipoMascota} - {self.Descripcion}'