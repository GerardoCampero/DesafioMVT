from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Appmvt.models import Familiares


# Create your views here.

# Se genera función de vista
def listadoFamiliares(request):

    # Se obtienen los datos de la tabla Familiares
    listaFamiliares = Familiares.objects.all()

    
    # Se genera un diccionario con la lista
    datos = {
        "listaFamiliares": listaFamiliares,

    }

    # Se obtiene el template html
    plantilla = loader.get_template("Template.html")
    
    # Se renderiza datos en la plantilla y se almacena en la variable documento
    documento =  plantilla.render(datos)
    
    # Retorna la variable documento
    return HttpResponse(documento)


