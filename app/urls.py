from django.urls import include,path
from .views import tipo_habitacion,tipo_habitacion_add, habitacion,habitacion_add

urlpatterns = [
    path('tipo_habitacion', tipo_habitacion, name='tipo_habitaicon'),
    path('tipo_habitacion_add', tipo_habitacion_add, name='tipo_habitacion_add'),
    path('habitacion_add', habitacion_add, name='habitacion_add'),
    path('habitacion', habitacion, name='habitacion')
]