from django.urls import include,path
from .views import tipo_habitacion,tipo_habitacion_add, tipo_habitacion_modif,tipo_habitacion_eliminar, habitacion_eliminar
from .views import tipo_habitacion,tipo_habitacion_add, habitacion,habitacion_add, index, habitacion_modif
from .views import index_usuario,verificarReserva,recepcionista
from .views import crear_cuenta, clientes, lista_clientes
from .views import modificar_perfil


urlpatterns = [
    path('tipo_habitacion', tipo_habitacion, name='tipo_habitacion'),
    path('tipo_habitacion_add', tipo_habitacion_add, name='tipo_habitacion_add'),
    path('habitacion_add', habitacion_add, name='habitacion_add'),
    path('habitacion', habitacion, name='habitacion'),
    path('habitacion_eliminar/<id>', habitacion_eliminar, name='habitacion_eliminar'),
    path('habitacion_modificar/<id>', habitacion_modif, name='habitacion_modif'),
    path('tipo_habitacion_modif/<id>', tipo_habitacion_modif, name='tipo_habitacion_modif'),
    path('tipo_habitacion_eliminar/<id>', tipo_habitacion_eliminar, name='tipo_habitacion_eliminar'),
    path('', index, name='index'),
    path('verificarReserva', verificarReserva, name='verificarReserva'), 
    path('recepcionista/<id>', recepcionista, name='recepcionista')
    path('index_usuario', index_usuario, name='index_usuario'),
    path('accounts/crear_cuenta', crear_cuenta, name='crear_cuenta'),
    path('modificar_perfil/<id>', modificar_perfil, name='modificar_perfil'),
    path('clientes', clientes, name= 'clientes'),
    path('lista_clientes/',lista_clientes, name='lista_clientes'),
]