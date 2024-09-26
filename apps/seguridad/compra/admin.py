from django.contrib import admin
from apps.seguridad.compra.models import Compra
# Register your models here.
@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    search_fields = ['Codigo_Compra', 'Descripcion', 'Fecha']
    list_display = ['Codigo_Compra', 'Descripcion', 'Fecha']