from django.urls import include,path
from .views import tipo_habitacion,tipo_habitacion_add

urlpatterns = [
    path('tipo_habitacion', tipo_habitacion, name='tipo_habitaicon'),
    path('tipo_habitacion_add', tipo_habitacion_add, name='tipo_habitacion_add')
]