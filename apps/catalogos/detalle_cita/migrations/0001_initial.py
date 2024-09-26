# Generated by Django 4.2 on 2024-09-25 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enfermedades', '0001_initial'),
        ('cita', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_Cita',
            fields=[
                ('ID_DetalleCita', models.AutoField(primary_key=True, serialize=False)),
                ('Codigo_DetalleCita', models.CharField(max_length=10, unique=True, verbose_name='Codigo de detalle cita')),
                ('Descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('ID_Cita', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cita.cita', verbose_name='Cita No')),
                ('ID_Enfermedades', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='enfermedades.enfermedades', verbose_name='Enfermedad')),
            ],
            options={
                'verbose_name': 'Detalles de Cita',
            },
        ),
    ]