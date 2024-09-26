from django.db import models

# Create your models here.
class Enfermedades(models.Model):
    ID_Enfermedades = models.AutoField(primary_key=True)
    Codigo_Enfermedades = models.CharField(max_length=10, verbose_name='Codigo de enfermedad', unique=True)
    Descripcion = models.CharField(max_length=200, verbose_name='Descripcion')

    class Meta:
        verbose_name = 'Enfermedade'

    def __str__(self):
        return f'{self.Codigo_Enfermedades} - {self.Descripcion}'