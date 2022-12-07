from django.urls import path
from appEmi.views import *

urlpatterns = [
    path("inicio/", inicio, name="apli-emi-inicio"),
    path("gradofamilia", gradofamilia, name="apli-emi-familiar"),
    path("edades/", edades,name="apli-emi-edades"),
    path("emails/", emails, name="apli-emi-emails"),
    path("nombres/", nombres, name="apli-emi-nombres"),
    #Clase PlayGInterM III:
    #path("familiar/crear/", creacion_familiar_nombre_edad, name="apli-emi-familiar-crear"), 
    path("conyugue/crear/", creacion_conyugue, name="apli-emi-conyugue-crear"), 
    path("conyugue/buscar/", buscar_conyugue, name="apli-emi-conyugue-buscar"), 
    path("familiar/buscar/", buscar_familiar, name="apli-emi-familiar-buscar"), 
    path("familiar/buscar/resultados/", resultados_busqueda_familiar, name="apli-emi-familiar-buscar-resultados"),
    
    path("familiares/crear/", creacion_familiar, name= "apli-emi-familiar-crear")
    
    #path("familia_formulario", views.familia_formulario,name="Familia_Formulario"),
    #path("fechanacimientos/", fechanacimientos),
           
]




