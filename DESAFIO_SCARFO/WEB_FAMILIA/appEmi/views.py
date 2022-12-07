
#import datetime
#from django.template import Template, Context, loader
from django.http import HttpResponse
from appEmi.models import Familiar, Conyugues
from appEmi.forms import ConyugueFormulario, FamiliarFormulario
from django.shortcuts import render


# def vista_formulario(request):
#    return render(request, "appEmi/familia_formulario.html")
def inicio(request):
    return render(request, "appEmi/index.html")

def gradofamilia(request):
    return render(request, "appEmi/gradofamilia.html")
   
    #return HttpResponse("Estas en gradofamilia")

def edades(request):
    return render(request, "appEmi/edades.html")
    #return HttpResponse("Estas en  edades")

def emails(request):
    return render(request, "appEmi/emails.html")


def creacion_familiar(request):
    
    if request.method == "POST":
        formulario= FamiliarFormulario(request.POST)
        if formulario.is_valid():
            #Accedemos al diccionario que contiene la informacion del formulario
            data= formulario.cleaned_data
            familiar=Familiar(nombre=data["nombre"], edad=data["edad"])
            familiar.save()
    formulario= FamiliarFormulario()
    return render (request, "appEmi/familiar_formulario.html" , {"formulario": formulario} )
    






#def familiares(request): # Clase PlayGAvanzado I 35´
 #   errores= ""
  # validamos tipo de peticion   
  #  if request.method == "POST": # validamos tipo de peticion
         #cargamos los datos en el formuario
   #     formulario= FamiliarFormulario(request.POST)
         #Validamos los datos
    #    if formulario.is_valid(): 
     #        #recuperamos los datos sanitizados
      #      data= formulario.cleaned_data
             #Creamos el familiar
       #     familiar=Familiar(nombre=data["nombre"], tipo_de_pariente=data["tipo_de_familiar"], email=data["email"])
            #Guardamos el familiar
        #    familiar.save()
        #else:
            # Si el formulario no es valido, guardamos los errores para mostrarlos
         #   errores= formulario.errors
    #Recuperar todos familiares de la BD    
    #familiares= Familiar.objects.all() # Obtener TODOS los registros de ese modelo
    #Creamos el formulario vacio
    #formulario= FamiliarFormulario()
    #Creamos el contexto
    #contexto= {"Listado_familiar": familiares, "formulario": formulario, "errores":errores}
    #Retornamos la respuesta
    #return render(request,"appEmi/nombres.html", contexto)        
        
        
        
        
    


 # def creacion_familiar_nombre_edad(request):   #Clase PlayGInterM III
 #   print(request.GET)
 #   print(request.POST)
 #   print(request.method)
 #   if request.method == "POST":      
 #         nombre_familiar = request.POST["nombre"]
 #         edad_familiar = request.POST["edad"]
 #         familiar=Familiar(nombre=nombre_familiar, edad=edad_familiar)
 #         familiar.save()       
 #   return render(request, "appEmi/familia_formulario_nombre_edad.html")


# Clase PlayGInterM III 
def creacion_conyugue(request):   
    
    if request.method == "POST":
        formulario= ConyugueFormulario(request.POST)
        
        #Validamos que el formulario no tenga problemas, is valid valida los datos y /// 
        #en caso de ser validos los datos, los carga en el formulario cleaned.data
        
        if formulario.is_valid(): #is_valid es un metodo, No una función, por lo tanto lleva ()            
             data= formulario.cleaned_data  #Recuperamos los datos del atributo cleaned_data
             conyugue= Conyugues(nombre=data["nombre"], tipo_de_pariente=data["tipo_de_pariente"], email=data["email"])        
             conyugue.save()
    formulario= ConyugueFormulario()
    contexto= {"formulario": formulario}   
    return render(request, "appEmi/conyugues_formulario.html", contexto)


def buscar_conyugue(request):
    if request.GET:
        nombre_conyugue= request.GET.get("nombre_conyugue","")
        if nombre_conyugue == "":
            conyugues= []
        else:
            conyugues= Conyugues.objects.filter(nombre__icontains=nombre_conyugue)
        return render(request, "appEmi/busqueda_conyugues.html", {"listado_conyugues":conyugues})
    
    return render(request, "appEmi/busqueda_conyugues.html", {"listado_conyugues": []})
        




 # Clase PlayGInterM III 
def buscar_familiar(request): 
    return render(request, "appEmi/busqueda_familiar.html")


# Clase PlayGInterM III 2h05` :    
def resultados_busqueda_familiar(request):
   # print(request.GET)
    nombre_familiar= request.GET["nombre_familiar"]
    familiar= Familiar.objects.filter(nombre__icontains=nombre_familiar)
    return render(request, "appEmi/resultados_busquedas_familiares.html", {"familiar": familiar})



# Clase PlayGAvanzado I 20´ a 30` :
def nombres(request):
    nombres= Familiar.objects.all() #Obtener TODOS los registros de ese modelo (ver modelo.py)
    contexto= {"listado_nombres": nombres}
    return render(request, "appEmi/nombres.html",contexto)
   #return HttpResponse("Estas en nombres")


    



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