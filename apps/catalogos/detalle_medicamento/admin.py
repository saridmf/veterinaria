from django.contrib import admin

from apps.catalogos.detalle_medicamento.models import DetalleMedicamento


# Register your models here.
@admin.register(DetalleMedicamento)
class DetalleMedicamentoAdmin(admin.ModelAdmin):
    search_fields = ['Cantidad', 'Descripcion']
    list_display = ['Descripcion', 'Cantidad', 'ID_Cita', 'ID_Medicamento']