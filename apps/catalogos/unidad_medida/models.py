from django.db import models

# Create your models here.
class UnidadMedida(models.Model):
    ID_Unidad_Medida = models.AutoField(primary_key=True)
    Codigo_Unidad_Medida = models.CharField(max_length=10, verbose_name='Codigo de unidad medida', unique=True)
    Descripcion = models.CharField(max_length=40, verbose_name='Descripcion')

    class Meta:
        verbose_name = 'Unidades de Medida'

    def __str__(self):
        return f'{self.Codigo_Unidad_Medida} - {self.Descripcion}'