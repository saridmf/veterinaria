from django.db import models

# Create your models here.
class Presentacion(models.Model):
    ID_Presentacion = models.AutoField(primary_key=True)
    Codigo_Presentacion = models.CharField(max_length=10, verbose_name='Codigo de presentacion', unique=True)
    Peso = models.CharField(max_length=40, verbose_name='Peso')

    class Meta:
        verbose_name = 'Presentacione'

    def __str__(self):
        return f'{self.Codigo_Presentacion} - {self.Peso}'