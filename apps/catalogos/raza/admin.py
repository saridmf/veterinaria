from django.contrib import admin

from apps.catalogos.raza.models import Raza


# Register your models here.
@admin.register(Raza)
class RazaAdmin(admin.ModelAdmin):
    search_fields = ['Codigo_Raza', 'Descripcion']
    list_display = ['Codigo_Raza', 'Descripcion', 'ID_TipoMascota']