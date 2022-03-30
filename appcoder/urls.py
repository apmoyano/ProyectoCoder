
from django.urls import path
from appcoder.views import Inicio
from appcoder.views import *

urlpatterns = [path('',Inicio, name= "inicio"),
path('viajes/', Viaje , name="viajes"),

path("viajes/buscar",buscarViaje, name= "buscar_viaje"),


path("viajes/list/",ViajeLista.as_view(), name= "viaje_list"),
path("viajes/nuevo/",CrearViaje.as_view(), name= "viaje_create"),
path("viajes/<pk>/",ViajeDetalle.as_view(), name= "viaje_detail"),
path("viajes/editar/<pk>/",UpdateViaje.as_view(), name= "viaje_update"),
path("viajes/borrar/<pk>/",DeleteViaje.as_view(), name= "viaje_delete"),
]