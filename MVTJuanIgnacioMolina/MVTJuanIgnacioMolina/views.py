from django.http import HttpResponse
from django.template import Template, Context

def saludo (request):
    return HttpResponse ("HOLA")

def ListaFamiliares(request):
    html = open('C:/Users/User/Desktop/Proyecto clase/pruebas/MVTJuanIgnacioMolina/MVTJuanIgnacioMolina/MVTJuanIgnacioMolina/Plantillas/Templates.html')

    plantilla = Template(html.read())

    html.close()

    Contexto = Context()

    documento = plantilla.render(Contexto)

    return HttpResponse(documento)