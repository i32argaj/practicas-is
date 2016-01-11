from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from liga.models import Equipo
# Create your views here.

def index(request):
	equipos=Equipo.objects.order_by('nombre')
	contexto={"equipos":equipos}
	return render(request,"home.html",contexto)
