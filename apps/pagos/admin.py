from django.contrib import admin
from .models import Transaccion

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('divisa', 'monto', 'nombre_quien_realiza', 'tipo_documento', 'creado_en')
    search_fields = ('nombre_quien_realiza', 'descripcion', 'divisa')
