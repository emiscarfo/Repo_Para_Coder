from django.http import HttpResponse
#from django.template import loader lo agregue dos lineas mas abajo con una ,
from datetime import datetime
from django.template import Template, Context, loader

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
    archivo= open(r"C:\Users\GAMER DELL\visual estudio EMI\DJANGO\DESAFIO_ENTREGABLE\DESAFIO_CODER\templates\plantilla_bonita.html")
    plantilla= Template(archivo.read())
    archivo.close()
    datos= {"nombre":"Emiliano", "fecha":datetime.now(),"apellido":"Scarfo","edad" :45.5}
    contexto= Context(datos)
    documento= plantilla.render(contexto)
    return HttpResponse(documento)

def vista_listado_alumnos(request):
    archivo= open(r"C:\Users\GAMER DELL\visual estudio EMI\DJANGO\DESAFIO_ENTREGABLE\DESAFIO_CODER\templates\listado_alumnos.html")
    plantilla= Template(archivo.read())
    archivo.close()
    listado_alumnos=["Susana Lewkow","Emiliano Scarfo",
    "Eva Araujo","Laura Barreiro","Pablo Sini",
    "Martin Recalt"]
    datos= {"Tecnologia":"TurboC", "listado_alumnos":listado_alumnos}
    contexto= Context(datos)
    documento= plantilla.render(contexto)
    return HttpResponse(documento)

def vista_listado_alumnos2(request):
    lista_alumnos=["Susana Lewkow","Emiliano Scarfo",
    "Eva Araujo","Laura Barreiro","Pablo Sini",
    "Martin Recalt"]
    datos= {"Tecnologia":"TurboC", "listado_alumnos":lista_alumnos}
    
    plantilla= loader.get_template("listado_alumnos.html")
    documento= plantilla.render(datos)
    return HttpResponse(documento)