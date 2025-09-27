from django.shortcuts import get_object_or_404
from .models import Transaccion
from .repositories import TransaccionRepository


class TransaccionService:
    def __init__(self, repo: TransaccionRepository | None = None):
        self.repo = repo or TransaccionRepository()

    def crear(self, data: dict) -> Transaccion:
        return self.repo.crear(**data)

    def listar(self):
        return self.repo.listar()

    def obtener(self, pk: int) -> Transaccion:
        return get_object_or_404(Transaccion, pk=pk)

    def actualizar(self, pk: int, data: dict) -> Transaccion:
        trans = self.obtener(pk)
        return self.repo.actualizar(trans, **data)

    def eliminar(self, pk: int) -> None:
        trans = self.obtener(pk)
        self.repo.eliminar(trans)
