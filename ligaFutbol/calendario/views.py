from django.shortcuts import render
from django.http import HttpResponse
from liga.models import Equipo
from .models import Partido, Jornada

# Create your views here.

def mostrarCalendario(request):
	jornadas=Jornada.objects.order_by('numero')
	contexto={"jornadas":jornadas}
	return render(request,"calendario.html",contexto)

def mostrarJornada(request, numeroJornada):
	jornada=Jornada.objects.get(numero=numeroJornada)
	partidos=Partido.objects.filter(jornada=jornada)
	partidos=partidos.order_by('dia')
	contexto={"partidos":partidos, "jornada":jornada}
	return render(request,"jornada.html",contexto)
