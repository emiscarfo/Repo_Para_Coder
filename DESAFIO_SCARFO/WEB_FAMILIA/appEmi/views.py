from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from appEmi.models import Familiar


# Create your views here.

def listado_familia(request):
    familiar= Familiar.objects.all()
    cadena_respueta= ""
    for familia in familiar:
        cadena_respueta += f"({familiar.nombre}, {familiar.tipo_de_pariente})" + "  "
        
    return HttpResponse(cadena_respueta)



def vista_usando_cargador_de_plantillas_loader(request):
    # Creamos el diccionario de datos
    listado_familiares = ["Emiliano Scarfo","Laura Gonzalez", "Eva Araujo", "Matias Scarfo", "Sofia Asen Scarfo", "Susana Lewkow"]
    datos= {"FAMILIA":"EMILIANO","lista_familia":listado_familiares}
    plantilla= loader.get_template("plantilla5.html")
    documento= plantilla.render(datos)
    return HttpResponse(documento)