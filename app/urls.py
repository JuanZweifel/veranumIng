from django.urls import include,path
from .views import tipo_habitacion,tipo_habitacion_add, tipo_habitacion_modif,tipo_habitacion_eliminar

urlpatterns = [
    path('tipo_habitacion', tipo_habitacion, name='tipo_habitacion'),
    path('tipo_habitacion_add', tipo_habitacion_add, name='tipo_habitacion_add'),
    path('tipo_habitacion_modif/<id>', tipo_habitacion_modif, name='tipo_habitacion_modif'),
    path('tipo_habitacion_eliminar/<id>', tipo_habitacion_eliminar, name='tipo_habitacion_eliminar'),
]