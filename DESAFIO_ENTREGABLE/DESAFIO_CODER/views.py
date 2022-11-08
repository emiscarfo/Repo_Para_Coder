from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def vista_saludo(request):
    return HttpResponse(""" <h1> Bienvenidos a mi pagina!  :) </h1>
     <p style='color:red' > Esto es una prueba </p> """)

def dia_hoy(request, nombre):
    hoy=datetime.now()

    respuesta= f"Hoy es {hoy} -Bienvenid@ {nombre}"
    return HttpResponse(respuesta)

def año_nacimiento(request, edad):
    edad= int(edad)
    año_nac= datetime.now().year - edad
    return HttpResponse(f"Naciste en {año_nac}")

def vista_plantilla(request):
    archivo=open(r"C:\Users\GAMER DELL\visual estudio EMI\DJANGO\DESAFIO_ENTREGABLE\DESAFIO_CODER\templates\plantilla_bonita.html")
    plantilla= Template(archivo.read())
    archivo.close()
    contexto=Context()
    documento=plantilla.render(contexto)
    return HttpResponse(documento)
