#encoding:utf-8
import json as simplejson
from actividades.forms import FormEstudiante, FormDocente, FormJefeDepartamento, FormActividad, FotoFormset, SoporteFormset, DocumentoFormset, FormUsuario, ChangePasswordForm
from django.contrib.auth.models import User
from actividades.models import Actividad, Asignatura

class ActividadService():
	instance = None
	
	@staticmethod
	def get_instance():
		if (ActividadService.instance==None):
			ActividadService.instance = ActividadService()
		#end if
		return ActividadService.instance
	#end def 

	def addEstudiante(self, request):
		if request.method == "POST":
			formUser = FormUsuario(request.POST)
			form = FormEstudiante(request.POST)
			if formUser.is_valid():
				if form.is_valid():
					add = form.save(commit=False)
					username = formUser.cleaned_data['username']
					password = formUser.cleaned_data['password_one']
					email = formUser.cleaned_data['email']
					u = User.objects.create_user(username=username, email=email,
												 password=password)
					u.set_password(raw_password=password)
					u.save()
					add.user = u
					add.save()
					return [True,'[{"mensaje":true}]']
				#end if
				errors = form.errors.items()
				return [True,simplejson.dumps(error)]
			#end if
			erros = formsUser.errors.items()
			return [True, simplejson.dumps(error)]
		#end if
		return [False, FormUsuario(), FormEstudiante()]
	#end def 
	
	def addDocente(self, request):
		if request.method == "POST":
			formUser = FormUsuario(request.POST)
			form = FormDocente(request.POST)
			if formUser.is_valid():
				if form.is_valid():
					add = form.save(commit=False)
					username = formUser.cleaned_data['username']
					password = formUser.cleaned_data['password_one']
					email = formUser.cleaned_data['email']
					u = User.objects.create_user(username=username, email=email,
												 password=password)
					u.set_password(raw_password=password)
					u.save()
					add.user = u
					add.save()
					return [True,'[{"mensaje":true}]']
				#end if
				errors = form.errors.items()
				return [True,simplejson.dumps(error)]
			#end if
			erros = formsUser.errors.items()
			return [True, simplejson.dumps(error)]
		#end if
		return [False, FormUsuario(), FormDocente()]
	#end def 

	def addJefe(self, request):
		if request.method == "POST":
			formUser = FormUsuario(request.POST)
			form = FormJefeDepartamento(request.POST)
			if formUser.is_valid():
				if form.is_valid():
					add = form.save(commit=False)
					username = formUser.cleaned_data['username']
					password = formUser.cleaned_data['password_one']
					email = formUser.cleaned_data['email']
					u = User.objects.create_user(username=username, email=email,
												 password=password)
					u.set_password(raw_password=password)
					u.save()
					add.user = u
					add.save()
					return [True,'[{"mensaje":true}]']
				#end if
				errors = form.errors.items()
				return [True,simplejson.dumps(error)]
			#end if
			erros = formsUser.errors.items()
			return [True, simplejson.dumps(error)]
		#end if
		return [False, FormUsuario(), FormJefeDepartamento()]
	#end def 

	def addActividad(self, request):
		if request.method == "POST":
			formA = FormActividad(request.POST)
			if formA.is_valid():
				form = formA.save(commit=False)
				formF = FotoFormset(request.POST, request.FILES, instance=form)
				formS = SoporteFormset(request.POST,request.FILES, instance=form)
				formD = DocumentoFormset(request.POST, request.FILES, instance=form)
				if formF.is_valid():
					if formS.is_valid():
						if formD.is_valid():
							form.save()
							formF.save()
							formS.save()
							formD.save()
							formA.save_m2m()
							return [True,'[{"mensaje":true}]']
						#end if
						errors = formD.errors.items()
						return [True, simplejson.dumps(errors)]
					#end if
					errors = formS.errors.items()
					return [True, simplejson.dumps(errors)]
				#end if
				errors = formF.errors.items()
				return [True,simplejson.dumps(errors)] 
			#end if
			errors = form.error.items()
			return [True, simplejson.dumps(errors)]
		#end if
		return [False, FormActividad(), FotoFormset(instance=Actividad()), SoporteFormset(instance=Actividad()),DocumentoFormset(instance=Actividad())]               
	#end def

	def editActividad(self, request, id):
		if request.method == "POST":
			formA = FormActividad(request.POST,instance=id)
			if formA.is_valid():
				form = formA.save(commit=False)
				formF = FotoFormset(request.POST, request.FILES, instance=form)
				formS = SoporteFormset(request.POST,request.FILES, instance=form)
				formD = DocumentoFormset(request.POST, request.FILES, instance=form)
				if formF.is_valid():
					if formS.is_valid():
						if formD.is_valid():
							form.save()
							formF.save()
							formS.save()
							formD.save()
							formA.save_m2m()
							return [True,'[{"mensaje":true}]']
						#end if
						errors = formD.errors.items()
						return [True, simplejson.dumps(errors)]
					#end if
					errors = formS.errors.items()
					return [True, simplejson.dumps(errors)]
				#end if
				errors = formF.errors.items()
				return [True,simplejson.dumps(errors)] 
			#end if
			errors = form.error.items()
			return [True, simplejson.dumps(errors)]
		#end if
		return [False, FormActividad(instance=id), FotoFormset(instance=id), SoporteFormset(instance=id),DocumentoFormset(instance=id)]               
	#end def 



	def filtroAB(self,request):
		data2 = "["
		anio1 = request.POST.get('anio1',False)
		anio2 = request.POST.get('anio2',False)
		periodo = request.POST.get('periodo',False)
		query = Actividad.objects.filter(estado=True)
		if anio1 and int(anio1) != 0 and int(anio2) == 0:
			if int(periodo) != 0:
				r1 = '["Actividades Periodo %d %s %d ",%d],'%(int(periodo),"año".decode('utf-8'), int(anio1), query.filter(anio=anio1, periodo=periodo).count())                  
				data2 += r1 
			else:    
				r1 = '["Actividades Periodo 1 %s %d ",%d],'%("año".decode('utf-8'), int(anio1), query.filter(anio=anio1, periodo=1).count())  
				r2 = '["Actividades Periodo 2 %s %d ",%d],'%("año".decode('utf-8'), int(anio1), query.filter(anio=anio1, periodo=2).count()) 
				data2 += r1 + r2 
			#end if
		elif anio1 and int(anio1) != 0 and anio2 and int(anio2) != 0:
			actividad = Actividad.objects.filter(anio__gte=anio1, anio__lte=anio2, estado=True).distinct('anio').values('anio')
			if int(periodo) != 0:
				for a in actividad:
					r1 = '["Actividades Periodo %d %s %d ",%d],'%(int(periodo),"año".decode('utf-8'), a['anio'], Actividad.objects.filter(anio=a['anio'], periodo=periodo).count())  
					data2 += r1 
				#end for
			else:
				for a in actividad:
					r1 = '["Actividades Periodo 1 %s %d ",%d],'%("año".decode('utf-8'), a['anio'], Actividad.objects.filter(anio=a['anio'], periodo=1).count())  
					r2 = '["Actividades Periodo 2 %s %d ",%d],'%("año".decode('utf-8'), a['anio'], Actividad.objects.filter(anio=a['anio'], periodo=2).count()) 
					data2 += r1 + r2
				#end for
		else: 
			anio = Actividad.objects.filter(estado=True).distinct('anio').values('anio')
			if int(periodo) != 0:
				for a in anio:
					r1 = '["Actividades Periodo %d %s %d ",%d],'%(int(periodo),"año".decode('utf-8'), a['anio'], Actividad.objects.filter(anio=a['anio'], periodo=periodo).count())  
					data2 += r1 
				#end for
			else:
				for a in anio:
					r1 = '["Actividades Periodo 1 %s %d ",%d],'%("año".decode('utf-8'), a['anio'], Actividad.objects.filter(anio=a['anio'], periodo=1).count())  
					r2 = '["Actividades Periodo 2 %s %d ",%d],'%("año".decode('utf-8'), a['anio'], Actividad.objects.filter(anio=a['anio'], periodo=2).count()) 
					data2 += r1 + r2
				#end for
		#end if
		data2 = data2[0:(len(data2) - 1)] + "]"
		barra2  = '{"chart":{"renderTo":"container","type":"column","margin":75,"options3d":{"enabled":true,"alpha":15,"beta":15,"depth":50,"viewDistance":25}},"title":{"text":"Actividades por '+"año".decode('utf-8')+'"},"plotOptions":{"column":{"depth":25}},"yAxis":{"opposite":false},"series":[{"name":"Cantidad","data":'+data2+'}]}'
		return "["+barra2+"]"
		#end def


	def filtroAP(self,request):
		data2 = "["
		anio1 = request.POST.get('anio1',False)
		anio2 = request.POST.get('anio2',False)
		periodo = request.POST.get('periodo',False)
		query = Actividad.objects.filter(estado=True)
		if anio1 and int(anio1) != 0 and int(anio2)==0:
			if int(periodo) != 0:
				r1 = '["Actividades Periodo %d %s %d ",%d],'%(int(periodo),"año".decode('utf-8'), int(anio1), query.filter(anio=anio1, periodo=periodo).count())                  
				data2 += r1 
			else:    
				r1 = '["Actividades Periodo 1 %s %d ",%d],'%("año".decode('utf-8'), int(anio1), query.filter(anio=anio1, periodo=1).count())  
				r2 = '["Actividades Periodo 2 %s %d ",%d],'%("año".decode('utf-8'), int(anio1), query.filter(anio=anio1, periodo=2).count()) 
				data2 += r1 + r2 
			#end for
		elif anio1 and int(anio1) != 0 and anio2 and int(anio2) != 0:
			actividad = Actividad.objects.filter(anio__gte=anio1, anio__lte=anio2, estado=True).distinct('anio').values('anio')
			if int(periodo) != 0:
				for a in actividad:
					r1 = '["Actividades Periodo %d %s %d ",%d],'%(int(periodo),"año".decode('utf-8'), a['anio'], Actividad.objects.filter(anio=a['anio'], periodo=periodo).count())  
					data2 += r1 
				#end for
			else:
				for a in actividad:
					r1 = '["Actividades Periodo 1 %s %d ",%d],'%("año".decode('utf-8'), a['anio'], Actividad.objects.filter(anio=a['anio'], periodo=1).count())  
					r2 = '["Actividades Periodo 2 %s %d ",%d],'%("año".decode('utf-8'), a['anio'], Actividad.objects.filter(anio=a['anio'], periodo=2).count()) 
					data2 += r1 + r2
				#end for
		else: 
			anio = Actividad.objects.filter(estado=True).distinct('anio').values('anio')
			if int(periodo) != 0:
				for a in anio:
					r1 = '["Actividades Periodo %d %s %d ",%d],'%(int(periodo),"año".decode('utf-8'), a['anio'], Actividad.objects.filter(anio=a['anio'], periodo=periodo).count())  
					data2 += r1 
				#end for
			else:
				for a in anio:
					r1 = '["Actividades Periodo 1 %s %d ",%d],'%("año".decode('utf-8'), a['anio'], Actividad.objects.filter(anio=a['anio'], periodo=1).count())  
					r2 = '["Actividades Periodo 2 %s %d ",%d],'%("año".decode('utf-8'), a['anio'], Actividad.objects.filter(anio=a['anio'], periodo=2).count()) 
					data2 += r1 + r2
				#end for
		#end if
		data2 = data2[0:(len(data2) - 1)] + "]"
		pie2 = '{"chart":{"type":"pie","options3d":{"enabled":true,"alpha":45,"beta":0}},"title":{"text":"Actividades por '+"año".decode('utf-8')+'"},"plotOptions":{"pie":{"allowPointSelect":true,"cursor":"pointer","depth":35,"dataLabels":{"enabled":true,"format":"{point.name}:  {point.percentage:.1f}%"}}},"series":[{"type":"pie","name":"Cantidad","data":'+data2+'}]}'
		return "["+pie2+"]"
	#end def

	def estadisticaActividad(self, request):
		asignaturas = Asignatura.objects.filter(estado=True)
		data = "["
		for a in asignaturas:
			r = '["%s",%d],'%(a.nombre, Actividad.objects.filter(asignatura__progacademica__asignatura=a).count())
			data += r
		#end for            
		data = data[0:(len(data) - 1)] + "]"
		barra  = '{"chart":{"renderTo":"container","type":"column","margin":75,"options3d":{"enabled":true,"alpha":15,"beta":15,"depth":50,"viewDistance":25}},"title":{"text":"Actividades por Asignatura"},"plotOptions":{"column":{"depth":25}},"yAxis":{"opposite":false},"series":[{"name":"Cantidad","data":'+data+'}]}'
		pie = '{"chart":{"type":"pie","options3d":{"enabled":true,"alpha":45,"beta":0}},"title":{"text":"Actividades por Asignatura"},"plotOptions":{"pie":{"allowPointSelect":true,"cursor":"pointer","depth":35,"dataLabels":{"enabled":true,"format":"{point.name}:  {point.percentage:.1f}%"}}},"series":[{"type":"pie","name":"Cantidad","data":'+data+'}]}'
		respuesta = "["+barra+","+ pie+"]"
		return respuesta
	#end def
#end class