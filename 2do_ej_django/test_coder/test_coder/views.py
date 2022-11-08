from django.http import HttpResponse
from datetime import datetime

def fecha_actual(request):
    hoy = datetime.now().strftime("%Y|%m|%d")
    return HttpResponse(hoy)
def inicio(request):
    # Leemos el contenido del archivo HTML
    archivo = open("/Users/leonelgareis/Documents/coder44470/ac_django/test_coder/test_coder/templates/inicio.html", "r")

    # Creamos una plantilla a partir del contenido del archivo
    plantilla = Template(archivo.read())

    # Cerramos el archivo porque no lo usamos mas
    archivo.close()
    
    # Creamos el contexto que necesita la plantilla
    contexto = Context()

    # Generar el documento a devolver al usuario
    documento = plantilla.render(contexto)
    
    return HttpResponse(documento)
