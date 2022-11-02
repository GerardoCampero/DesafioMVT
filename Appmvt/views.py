from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Appmvt.models import Familiares


# Create your views here.

# Se genera función de vista
def listadoFamiliares(request):

    listaFamiliares = Familiares.objects.all()

    
    
    datos = {
        "listaFamiliares": listaFamiliares,

    }

    plantilla = loader.get_template("Template.html")

    documento =  plantilla.render(datos)

    return HttpResponse(documento)


