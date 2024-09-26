from django.contrib import admin

from apps.seguridad.detalle_compra.models import DetalleCompra


# Register your models here.
@admin.register(DetalleCompra)
class DetalleCompraAdmin(admin.ModelAdmin):
    search_fields = ['ID_Medicamento', 'Precio', 'Cantidad', 'ID_Compra']
    list_display =  ['ID_Medicamento', 'Precio', 'Cantidad', 'ID_Compra']