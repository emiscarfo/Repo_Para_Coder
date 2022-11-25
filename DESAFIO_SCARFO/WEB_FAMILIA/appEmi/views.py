
#import datetime
#from django.template import Template, Context, loader
from django.http import HttpResponse
from appEmi.models import Familiar
from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "appEmi/index.html")

def nombres(request):
    return render(request, "appEmi/nombres.html")
    #return HttpResponse("Estas en nombres")

def gradofamilia(request):
    return render(request, "appEmi/gradofamilia.html")
   
    #return HttpResponse("Estas en gradofamilia")

def edades(request):
    return render(request, "appEmi/edades.html")
    #return HttpResponse("Estas en  edades")

def emails(request):
    return render(request, "appEmi/emails.html")
    #return HttpResponse("Estas en  emails")

#def fechanacimientos(request):
    #return render(request, "appEmi/fechanacimientos.html")
#    return HttpResponse("Estas en fecha de nacimientos")

#def listado_familia(request):
#       familiar= Familiar.objects.all()
#       cadena_respueta= ""
#       for familia in familiar:
#           cadena_respueta += f"({familiar.nombre}, {familiar.tipo_de_pariente})" + "  "
#        return HttpResponse(cadena_respueta)



#def vista_usando_cargador_de_plantillas_loader(request):
#   Creamos el diccionario de datos
#   listado_familiares = ["Emiliano Scarfo","Laura Gonzalez", "Eva Araujo", "Matias Scarfo", "Sofia Asen Scarfo", "Susana Lewkow"]
#   datos= {"FAMILIA":"EMILIANO","lista_familia":listado_familiares}
#   plantilla= loader.get_template("plantilla5.html")
#   documento= plantilla.render(datos)
#   return HttpResponse(documento)