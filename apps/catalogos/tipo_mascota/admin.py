from django.contrib import admin

from apps.catalogos.tipo_mascota.models import TipoMascota


# Register your models here.
@admin.register(TipoMascota)
class TipoMascotaAdmin(admin.ModelAdmin):
    search_fields = ['Codigo_TipoMascota', 'Descripcion']
    list_display = ['Codigo_TipoMascota', 'Descripcion']