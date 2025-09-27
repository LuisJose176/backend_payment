from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .serializers import TransaccionSerializer
from .services import TransaccionService


class SoloAdminPuedeModificar(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ('create', 'list', 'retrieve'):
            return True
        return request.user and request.user.is_authenticated


class TransaccionViewSet(viewsets.ViewSet):
    permission_classes = [SoloAdminPuedeModificar]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = TransaccionService()

    def create(self, request):
        serializer = TransaccionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        trans = self.service.crear(serializer.validated_data)

        return Response({
            "status": True,
            "message": "Transacción registrada con éxito",
            "data": TransaccionSerializer(trans).data
        }, status=status.HTTP_201_CREATED)

    def list(self, request):
        data = self.service.listar()
        return Response({
            "status": True,
            "message": "Lista de transacciones obtenida correctamente",
            "data": TransaccionSerializer(data, many=True).data
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        trans = self.service.obtener(pk)
        return Response({
            "status": True,
            "message": "Detalle de la transacción",
            "data": TransaccionSerializer(trans).data
        }, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        serializer = TransaccionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        trans = self.service.actualizar(pk, serializer.validated_data)

        return Response({
            "status": True,
            "message": "Transacción actualizada con éxito",
            "data": TransaccionSerializer(trans).data
        }, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        trans = self.service.obtener(pk)
        serializer = TransaccionSerializer(trans, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        trans = self.service.actualizar(pk, serializer.validated_data)

        return Response({
            "status": True,
            "message": "Transacción actualizada parcialmente con éxito",
            "data": TransaccionSerializer(trans).data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        self.service.eliminar(pk)
        return Response({
            "status": True,
            "message": "Transacción eliminada con éxito"
        }, status=status.HTTP_204_NO_CONTENT)
