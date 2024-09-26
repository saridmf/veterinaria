from django.db import models

# Create your models here.
class Compra(models.Model):
    ID_Compra = models.AutoField(primary_key=True)
    Codigo_Compra = models.CharField(max_length=10, verbose_name='Codigo de compra', unique=True)
    Descripcion = models.CharField(max_length=200, verbose_name='Descripcion')
    Fecha = models.DateField(verbose_name='Fecha')

    class Meta:
        verbose_name = 'Compra'

    def __str__(self):
        return f'{self.Codigo_Compra} - {self.Descripcion}'