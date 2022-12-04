
from django.http import HttpResponse
from .models import Familiar
from datetime import date
from django.template import Template, Context, loader
from django.shortcuts import render


# Create your views here.
def Familia(request):
    lista_flia = Familiar.objects.all()
    return render(request, "Templates.html", {"lista_familiares": lista_flia})
