from django.contrib import admin

from apps.catalogos.presentacion.models import Presentacion


# Register your models here.
@admin.register(Presentacion)
class PresentacionAdmin(admin.ModelAdmin):
    search_fields = ['Codigo_Presentacion', 'Peso']
    list_display = ['Codigo_Presentacion', 'Peso']