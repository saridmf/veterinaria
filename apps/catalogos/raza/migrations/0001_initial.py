# Generated by Django 4.2 on 2024-09-25 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tipo_mascota', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('ID_Raza', models.AutoField(primary_key=True, serialize=False)),
                ('Codigo_Raza', models.CharField(max_length=10, unique=True, verbose_name='Codigo de raza')),
                ('Descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('ID_TipoMascota', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tipo_mascota.tipomascota', verbose_name='Tipo de Mascota')),
            ],
            options={
                'verbose_name': 'Raza',
            },
        ),
    ]
