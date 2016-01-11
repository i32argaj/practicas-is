from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Equipo, Jugadore
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render,render_to_response, redirect
from .forms import *

# Create your views here.

def mostrarClasificacion(request):
	equipos=Equipo.objects.order_by('-puntos')
	contexto={"equipos":equipos}
	return render(request,"liga.html",contexto)

def mostrarEquipo(request, nombreEquipo):
	equipo=Equipo.objects.get(nombreSimple__iexact=nombreEquipo)
	jugadores=Jugadore.objects.filter(equipo=equipo)
	jugadores=jugadores.order_by('posicion')
	contexto={"equipo":equipo, "jugadores":jugadores}
	return render(request,"equipo.html",contexto)

def crearEquipo(request):
	if request.method=="POST":
		equipo=Equipo()
		formulario=EquipoForm(request.POST,request.FILES,instance=equipo)
		if formulario.is_valid():
			formulario.save()
			return redirect('/')
	else:
		formulario=EquipoForm()
	context={'formulario':formulario}
	return render(request,"equipo_new.html",context)
	
@login_required()
def modificarEquipo(request, nombreEquipo):
	equipo=Equipo.objects.get(nombreSimple__iexact=nombreEquipo)
	if request.method=="POST":
		formulario=EquipoForm(request.POST,request.FILES,instance=equipo)
		if formulario.is_valid():
			formulario.save()
			return redirect('/')
	else:
		formulario=EquipoForm(instance=equipo)
	context={'formulario':formulario}
	return render(request,"equipo_mod.html",context)
