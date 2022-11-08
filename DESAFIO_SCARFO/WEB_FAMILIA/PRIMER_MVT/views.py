from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime
# from appfamiliar.models import *


def fecha_actual(request):
    hoy=datetime.now().strftime("%d|%m|%Y")
    return HttpResponse(f"Fecha actual: {hoy}")

def inicio(request):
   
    archivo = open(r"C:\Users\GAMER DELL\visual estudio EMI\DJANGO\DESAFIO_SCARFO\WEB_FAMILIA\PRIMER_MVT\templates\inicio.html","r")
    inicio=Template(archivo.read())
    archivo.close()
    datos = {"nombre": "Emiliano", "apellido": "Scarfo","fecha":datetime.now()}
    contexto= Context(datos)
    documento= inicio.render(contexto)
    return HttpResponse(documento)




    