from django.contrib import admin

from apps.catalogos.detalle_cita.models import Detalle_Cita


# Register your models here.
@admin.register(Detalle_Cita)
class Detalle_CitaAdmin(admin.ModelAdmin):
    search_fields = ['Codigo_DetalleCita']
    list_display = ['Codigo_DetalleCita', 'Descripcion', 'ID_Enfermedades', 'ID_Cita']