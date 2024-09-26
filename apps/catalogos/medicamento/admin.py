from django.contrib import admin

from apps.catalogos.medicamento.models import Medicamento


# Register your models here.
@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    search_fields = ['Codigo_Medicamento', 'Descripcion', 'ID_Presentacion']
    list_display = ['Codigo_Medicamento', 'Descripcion', 'ID_Presentacion', 'ID_Unidad_Medida', 'Precio', ]