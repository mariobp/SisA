#encoding:utf-8
from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Semestre(models.Model):
	#BOOL_CHOICES = ((1, 'Primer Periodo'), (2, 'Segundo Periodo'))
	nombre = models.CharField(max_length=200)
	#periodo = models.IntegerField(choices=BOOL_CHOICES)
	#anio = models.IntegerField("Año",max_length=4,default=date.today().year)
	estado = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre
	#end def 
#end class	

class Sede(models.Model):
	nombre = models.CharField(max_length=200)
	estado = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre
	#end def
#end class 

class Facultad(models.Model):
	nombre = models.CharField(max_length=200)
	sede = models.ForeignKey(Sede)
	estado = models.BooleanField(default=True)
	
	class Meta:
	    verbose_name = "Facultad"
	    verbose_name_plural = "Facultades"
	#end class

	def __unicode__(self):
		return self.nombre
	#end def
#end class

class Programa(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField(max_length=500)
	facultad = models.ForeignKey(Facultad)
	estado = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre
	#end def
#end class

class Persona(models.Model):
	user = models.OneToOneField(User)
	BOOL_CHOICES = ((True, 'Hombre'), (False, 'Mujer'))
	nombre = models.CharField("* Nombres", max_length=200)
	apellidos = models.CharField("* Apellidos", max_length=200)
	fecha_Nacimiento = models.DateField("* Fecha de Nacimiento")
	sexo = models.BooleanField("* Sexo", choices=BOOL_CHOICES, blank=False, default=True)
	identificacion = models.CharField("* Identificación", max_length=200, unique=True)
	telefono = models.IntegerField("* Telefono")
	direcion = models.CharField("* Dirección", max_length=400)
	estado = models.BooleanField(default=True)

	class Meta:
		abstract = True
		ordering = ['nombre']
	#end Class

	def save(self, *args, **kwargs):
		self.nombre = self.nombre.title()
		self.apellidos = self.apellidos.title()
		super(Persona, self).save(*args, **kwargs)
    #end def

 	def __unicode__(self):
 		nombre = "%s %s" % (self.nombre, self.apellidos)
 		return nombre
    #end def
#end class

class Estudiante(Persona):
	codigo = models.IntegerField("* Codigo",unique=True)
	semestre = models.ForeignKey(Semestre, verbose_name="* Semestre")
	programa = models.ForeignKey(Programa, verbose_name="* Programa")
#end class

class Docente(Persona):
	codigo = models.IntegerField(unique=True)
#end class

class JefeDepartamento(Persona):
	codigo = models.IntegerField(unique=True)

	class Meta:
		verbose_name = "Jefe de Departamento"
		verbose_name_plural = "Jefes de Departamento"
#end class

class PlanEstudio(models.Model):
	nombre = models.CharField(max_length=200)
	programa = models.ForeignKey(Programa)

	class Meta:
		verbose_name = "Plan de Estudio"
		verbose_name_plural = "Plan de Estudios"
	#end class

	def __unicode__(self):
		return self.nombre
	#end def
#end class

class Asignatura(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField(max_length=500)
	estado = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre
	#end def
#end class

class ProgAcademica(models.Model):
	BOOL_CHOICES = ((1, 'Primer Periodo'), (2, 'Segundo Periodo'))
	periodo = models.IntegerField(choices=BOOL_CHOICES)
	asignatura = models.ForeignKey(Asignatura)
	planestudio = models.ForeignKey(PlanEstudio, verbose_name='Plan de Estudio')
	anio = models.IntegerField("Año",default=date.today().year)

	class Meta:
		verbose_name = "Programacón Académica"
		verbose_name_plural = "Programaciones Académicas"
	#end class

	def __unicode__(self):
		nombre = "%s %s periodo %d %d"%(self.planestudio.nombre,self.asignatura.nombre,self.periodo, self.anio)
		return nombre
	#end def
#end class 

class AsignacionAsi(models.Model):
	progacademica = models.ForeignKey(ProgAcademica,verbose_name='Programacón Academica')
	docente = models.ForeignKey(Docente)
	estudiantes = models.ManyToManyField(Estudiante)
	anio = models.IntegerField("Año", default=date.today().year)
	estado = models.BooleanField(default=True)

	class Meta:
		verbose_name = "Asignación de Asignatura"
		verbose_name_plural = "Asinaciones de Asignatura"
	#end class 
	
	def __unicode__(self):
		nombre = "%s %d"%(self.progacademica.asignatura.nombre, self.anio)
		return nombre
	#end def 
#end def

class Tipo(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField(max_length=600)
	estado = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre
    #end def
#end class

class Actividad(models.Model):
	BOOL_CHOICES = ((1, 'Primer Periodo'), (2, 'Segundo Periodo'))
	nombre = models.CharField(max_length=200)
	periodo = models.IntegerField(choices=BOOL_CHOICES)
	tipo = models.ForeignKey(Tipo)
	jefe = models.ForeignKey(JefeDepartamento)
	asignatura = models.ManyToManyField(AsignacionAsi)
	objetivo = models.TextField(max_length=600)
	anio = models.IntegerField("Año",default=date.today().year)
	estado = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre
	#end def 
#end class

class Foto(models.Model):
    imagen = models.ImageField(upload_to='actividad/fotos', null=True, blank=True)
    actividad = models.ForeignKey(Actividad)

    def clean(self):
    	if self.imagen:
        	if self.imagen.size > 5*1024*1024:
        		raise ValidationError("La imagen no puede exceder los 5MB")
            #end if
        #end if
    #end def

    def thumbnail(self):
		return '<a href="/media/%s"><img src="/media/%s" width=50px heigth=50px/></a>' % (self.imagen, self.imagen)
    #end def

    thumbnail.allow_tags = True

    def __unicode__(self):
    	return self.actividad.nombre
    #end def 
#end class

class Soporte(models.Model):
	archivo = models.FileField(upload_to='actividad/soportes', null=True, blank=True)
	actividad = models.ForeignKey(Actividad)

	def clean(self):
		if self.archivo:
			if self.archivo.size > 5*1024*1024:
				raise ValidationError("La imagen no puede exceder los 5MB")
            #end if
        #end if
    #end def

	def __unicode__(self):
		return self.actividad.nombre
	#end def
#end class 

class Documento(models.Model):
	archivo = models.FileField(upload_to='actividad/documentos', null=True, blank=True)
	actividad = models.ForeignKey(Actividad)

	def clean(self):
		if self.archivo:
			if self.archivo.size > 5*1024*1024:
				raise ValidationError("La imagen no puede exceder los 5MB")
            #end if
        #end if
    #end def

	def __unicode__(self):
		return self.actividad.nombre
	#end def
#end class 