from django.contrib import admin

from apps.catalogos.estado_de_cita.models import EstadodeCita


# Register your models here.
@admin.register(EstadodeCita)
class EstadodeCitaAdmin(admin.ModelAdmin):
    search_fields = ['Codigo_EstadoCita', 'Descripcion']
    list_display = ['Codigo_EstadoCita', 'Descripcion']