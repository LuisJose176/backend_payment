from django.urls import path
from .views import TransaccionViewSet


transaccion_list = TransaccionViewSet.as_view({'get': 'list'})
transaccion_create = TransaccionViewSet.as_view({'post': 'create'})
transaccion_update = TransaccionViewSet.as_view({'put': 'update', 'patch': 'partial_update'})
transaccion_delete = TransaccionViewSet.as_view({'delete': 'destroy'})

urlpatterns = [
    path('transacciones/listar/', transaccion_list, name='transaccion-list'),
    path('transacciones/crear/', transaccion_create, name='transaccion-create'),
    path('transacciones/editar/<int:pk>/', transaccion_update, name='transaccion-update'),
    path('transacciones/eliminar/<int:pk>/', transaccion_delete, name='transaccion-delete'),

    path('transacciones/listar', transaccion_list),
    path('transacciones/crear', transaccion_create),
    path('transacciones/editar/<int:pk>', transaccion_update),
    path('transacciones/eliminar/<int:pk>', transaccion_delete),
]
