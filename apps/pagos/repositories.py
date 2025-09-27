from .models import Transaccion

class TransaccionRepository:
    def crear(self, **data) -> Transaccion:
        return Transaccion.objects.create(**data)

    def listar(self):
        return Transaccion.objects.all()

    def obtener(self, pk: int) -> Transaccion:
        return Transaccion.objects.get(pk=pk)

    def actualizar(self, instancia: Transaccion, **data) -> Transaccion:
        for k, v in data.items():
            setattr(instancia, k, v)
        instancia.save()
        return instancia

    def eliminar(self, instancia: Transaccion) -> None:
        instancia.delete()
