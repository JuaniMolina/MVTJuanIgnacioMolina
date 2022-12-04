from django.http import HttpResponse
from datetime import *
from django.template import Template, Context, loader


def saludo (request):
    return HttpResponse ("HOLA")

def ListaFamiliares(request):
    nom = "Juan"
    ap = "Molina"
    nacimiento = datetime(1989, 8, 12)

    diccionario = {'nombre': nom ,'apellido': ap, 'nacimiento':datetime.date(nacimiento) }  
    
    #html = open('C:/Users/User/Desktop/Proyecto clase/pruebas/MVTJuanIgnacioMolina/MVTJuanIgnacioMolina/MVTJuanIgnacioMolina/Plantillas/Templates.html')

    #plantilla = Template(html.read())

    #html.close()

    #Contexto = Context()

    #documento = plantilla.render(Contexto)

    plantilla = loader.get_template('Templates.html')

    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)