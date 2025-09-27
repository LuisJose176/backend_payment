from rest_framework import serializers
from .models import Transaccion

class TransaccionSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(source="nombre_quien_realiza", read_only=True)

    class Meta:
        model = Transaccion
        fields = [
            "id",
            "divisa",
            "monto",
            "descripcion",
            "nombre_quien_realiza",  
            "nombre",                
            "tipo_documento",
            "numero_tarjeta",
            "fecha_vencimiento",
            "codigo_seguridad",
            "creado_en",
        ]
        extra_kwargs = {
            "creado_en": {"read_only": True},
            "nombre_quien_realiza": {"write_only": True},
        }
