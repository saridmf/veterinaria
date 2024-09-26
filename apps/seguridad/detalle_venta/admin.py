from django.contrib import admin

from apps.seguridad.detalle_venta.models import DetalleVenta


# Register your models here.
@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    search_fields = ['Cantidad', 'Precio', 'ID_Venta', 'ID_Medicamento']
    list_display = ['ID_Medicamento', 'ID_Venta', 'Cantidad', 'Precio']