from django.contrib import admin

from apps.catalogos.cita.models import Cita


# Register your models here.
@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    search_fields = ['Codigo_Cita']
    list_display = ['Codigo_Cita', 'Fecha_Realizacion', 'Fecha_de_Cita', 'ID_EstadoCita', 'ID_Mascota', 'Peso']