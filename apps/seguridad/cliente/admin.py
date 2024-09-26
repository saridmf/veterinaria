from django.contrib import admin

from apps.seguridad.cliente.models import Cliente


# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['Codigo_Cliente', 'Nombres', 'Apellido1', 'Apellido2']
    list_display = ['Codigo_Cliente', 'Nombres', 'Apellido1', 'Apellido2', 'Telefono', 'Correo', 'Telefono']