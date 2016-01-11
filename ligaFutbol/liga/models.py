class Equipo(models.Model):
	nombre=models.CharField(max_length=100)
	nombreSimple=models.CharField(max_length=100)
	estadio=models.CharField(max_length=300)
	fotoEstadio=models.ImageField()
	ciudad=models.CharField(max_length=100)
	escudo=models.ImageField()
	puntos=models.IntegerField(default=0)
	entrenador=models.CharField(max_length=100)
	anio=models.IntegerField(default=0)
	breveHistoria=models.TextField(max_length=500)
	partidosJugados=models.IntegerField(default=0)
	partidosGanados=models.IntegerField(default=0)
	partidosPerdidos=models.IntegerField(default=0)
	partidosEmpatados=models.IntegerField(default=0)
	def __unicode__(self):
		return self.nombre

class Jugadore(models.Model):
	delantero="Delantero"
	centrocampista="Centrocampista"
	defensa="Defensa"
	portero="Portero"
	opcionesPosicion=((delantero, 'Delantero'), (centrocampista, 'Centrocampista'), (defensa, 'Defensa'), (portero, 'Portero')) 
	nombre=models.CharField(max_length=100)
	posicion=models.CharField(max_length=100, choices=opcionesPosicion)
	equipo=models.ForeignKey(Equipo)
	edad=models.IntegerField()
	goles=models.IntegerField(default=0)
	dorsal=models.IntegerField()
	def __unicode__(self):
		return self.nombre
