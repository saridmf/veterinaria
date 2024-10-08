# Generated by Django 4.2 on 2024-09-25 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('ID_Cliente', models.AutoField(primary_key=True, serialize=False)),
                ('Codigo_cliente', models.CharField(max_length=10, unique=True, verbose_name='Codigo de clientes*')),
                ('Nombres', models.CharField(max_length=20, verbose_name='Nombres*')),
                ('Apellido1', models.CharField(max_length=20, verbose_name='Apellido1*')),
                ('Apellido2', models.CharField(blank=True, max_length=20, null=True, verbose_name='Apellido2')),
                ('Correo', models.EmailField(max_length=254, verbose_name='Correo*')),
                ('Telefono', models.CharField(blank=True, max_length=12, null=True, verbose_name='Telefono')),
                ('Direccion', models.CharField(blank=True, max_length=150, null=True, verbose_name='Direccion')),
            ],
            options={
                'verbose_name': 'Cliente',
            },
        ),
    ]
