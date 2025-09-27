from django.db import models

class Transaccion(models.Model):
    DIVISA_OPCIONES = [
        ('COP', 'Peso Colombiano'),
        ('USD', 'Dólar Estadounidense'),
    ]
    TIPO_DOC_OPCIONES = [
        ('CC', 'Cédula'),
        ('PP', 'Pasaporte'),
    ]

    divisa = models.CharField(max_length=3, choices=DIVISA_OPCIONES)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    descripcion = models.TextField()
    nombre_quien_realiza = models.CharField(max_length=200)
    tipo_documento = models.CharField(max_length=2, choices=TIPO_DOC_OPCIONES)
    numero_tarjeta = models.CharField(max_length=16)
    fecha_vencimiento = models.CharField(max_length=5)  
    codigo_seguridad = models.CharField(max_length=4)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Transacciones'
        ordering = ['-creado_en']

    def __str__(self):
        return f"{self.nombre_quien_realiza} - {self.monto} {self.divisa}"
