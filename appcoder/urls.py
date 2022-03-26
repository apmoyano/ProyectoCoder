
from django.urls import path
from appcoder.views import Inicio
from appcoder.views import *

urlpatterns = [path('',Inicio),
path('pasajero/', Pasajero, name="Pasajero"),
path('aeropuerto/', Aeropuerto),
path('vuelo/', Vuelo),
]
