from django.db import models

# Create your models here.
class Cliente(models.Model):
    ID_Cliente = models.AutoField(primary_key=True)
    Codigo_Cliente = models.CharField(max_length=10, verbose_name='Código de clientes*', unique=True)
    Nombres = models.CharField(max_length=20, verbose_name='Nombres*')
    Apellido1 = models.CharField(max_length=20, verbose_name='Primer Apellido*')
    Apellido2 = models.CharField(max_length=20, verbose_name='Segundo Apellido', null=True, blank=True)
    Correo = models.EmailField(verbose_name='Correo*')
    Telefono = models.CharField(max_length=12, verbose_name='Teléfono', null=True, blank=True)
    Direccion = models.CharField(max_length=150, verbose_name='Dirección', null=True, blank=True)


    class Meta:
        verbose_name = 'Cliente'

    def __str__(self):
        return f'{self.Codigo_Cliente} - {self.Nombres}  {self.Apellido1}  {self.Apellido2}'