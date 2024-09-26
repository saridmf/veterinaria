from django.contrib import admin

from apps.seguridad.venta.models import Venta


# Register your models here.
@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    search_fields = ['Codigo_Venta', 'Descripcion', 'Fecha', 'ID_Cliente']
    list_display = ['Codigo_Venta', 'ID_Cliente', 'Descripcion', 'Fecha']