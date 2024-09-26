from django.contrib import admin

from apps.catalogos.enfermedades.models import Enfermedades


# Register your models here.
@admin.register(Enfermedades)
class EnfermedadesAdmin(admin.ModelAdmin):
    search_fields = ['Codigo_Enfermedades', 'Descripcion']
    list_display = ['Codigo_Enfermedades', 'Descripcion']