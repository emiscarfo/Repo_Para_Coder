
from django.contrib import admin
from django.urls import path, include
# from PRIMER_MVT.views import *
# from appEmi.views import * ya no es necesario porque incorpore el urls propio dentro de la appEmi

urlpatterns = [
    path('admin/', admin.site.urls),
    path("Emi/", include("appEmi.urls")),
    
    #path("fecha/", fecha_actual),
    #path("inicio/", inicio),
    #path("ver-familia/", vista_familia),
    #path("listado-familiares/", listado_familia),
]
  
    
