from django.contrib import admin

from apps.catalogos.unidad_medida.models import UnidadMedida


# Register your models here.
@admin.register(UnidadMedida)
class UnidadMedidaAdmin(admin.ModelAdmin):
    search_fields = ['Codigo_Unidad_Medida', 'Descripcion']
    list_display = ['Codigo_Unidad_Medida', 'Descripcion' ]