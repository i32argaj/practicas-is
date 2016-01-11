from django.db import models
from liga.models import Equipo
# Create your models here.

class Jornada(models.Model):
	numero=models.IntegerField(default=0)
	acabada=models.BooleanField(default=False)
	def __unicode__(self):
		return unicode(self.numero)
		
class Partido(models.Model):
	jornada=models.ForeignKey(Jornada)
	dia=models.DateField()
	equipoLocal=models.ForeignKey(Equipo,related_name='local')
	equipoVisitante=models.ForeignKey(Equipo,related_name='visitante')
	resultado=models.CharField(max_length=10)
	def __unicode__(self):
		return self.equipoLocal.nombre+"/"+self.equipoVisitante.nombre
