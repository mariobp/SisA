#encoding:utf-8
from django.shortcuts import render
from actividades.models import Actividad, Tipo, Asignatura, Estudiante, Docente, JefeDepartamento, AsignacionAsi,Foto, Soporte, Documento
from actividades.services import ActividadService
from SisA.settings import LOGIN_URL
from django.contrib.auth.decorators import login_required
import json as simplejson
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@login_required(login_url=LOGIN_URL)
def actividades(request):
	docente = Docente.objects.filter(user=request.user)
	tipo = Tipo.objects.filter(estado=True)
	asignatura = AsignacionAsi.objects.filter(estado=True).values('progacademica__asignatura__nombre','id')
	anio = Actividad.objects.filter(estado=True).distinct('anio')
	if docente:
		return render(request,'actividades/actividades.html',{'tipo':tipo,'asignatura':asignatura, 'anio':anio.values('anio'), 'add':True})
	#end if
	return render(request,'actividades/actividades.html',{'tipo':tipo,'asignatura':asignatura, 'anio':anio.values('anio'), 'add':False})
#end def 


def wsListActividades(request):
	docente = Docente.objects.filter(user=request.user).first()
	colums = ['nombre', 'tipo','anio']
	search = request.GET.get('search[value]', '')
	start  = request.GET.get('start', 0)
	orderc = request.GET.get('order[0][column]', '0')
	orderd = request.GET.get('order[0][dir]', 'desc')
	length = request.GET.get('length', 0)
	tipo = request.GET.get('columns[1][search][value]',0)
	asignatura = request.GET.get('columns[2][search][value]',0)
	anio = request.GET.get('columns[3][search][value]',0)
	anio2 = request.GET.get('columns[0][search][value]',0)
	periodo = request.GET.get('columns[4][search][value]',0)
	totalFiltered = Actividad.objects.filter(estado=True).count()
	query = Actividad.objects.filter(nombre__icontains=search, estado=True)
	if tipo != "" and int(tipo) != 0:
		query = query.filter(nombre__icontains=search, tipo=tipo, estado=True)
	if asignatura != "" and int(asignatura) != 0:
		query = query.filter(nombre__icontains=search, asignatura__in=asignatura, estado=True)
	if periodo != "" and int(periodo) != 0:
		query = query.filter(nombre__icontains=search, periodo=periodo, estado=True)
	if anio != "" and int(anio) != 0 and anio2=="":
		query = query.filter(nombre__icontains=search, anio=anio, estado=True)
	if anio2 != "" and int(anio2) != 0:
		query = query.filter(nombre__icontains=search, anio__gte=anio, anio__lte=anio2, estado=True)
	#end if
	recordsFiltered = query.count()
	if docente:
		if orderd == "asc":
			data = list(query.values('nombre','tipo__nombre','objetivo','anio','jefe__nombre','jefe__apellidos','id','periodo').order_by("-"+colums[int(orderc)])[int(start):int(length)+int(start)])
		else:
			data = list(query.values('nombre','tipo__nombre','objetivo','anio','jefe__nombre','jefe__apellidos','id','periodo').order_by(colums[int(orderc)])[int(start):int(length)+int(start)])
	else:
		if orderd == "asc":
			data = list(query.values('nombre','tipo__nombre','objetivo','anio','jefe__nombre','jefe__apellidos','id','periodo','estado').order_by("-"+colums[int(orderc)])[int(start):int(length)+int(start)])
		else:
			data = list(query.values('nombre','tipo__nombre','objetivo','anio','jefe__nombre','jefe__apellidos','id','periodo','estado').order_by(colums[int(orderc)])[int(start):int(length)+int(start)])
	#end if
	json = simplejson.dumps({'recordsTotal':totalFiltered, 'recordsFiltered':recordsFiltered, 'data':data})
	#end if
	return HttpResponse(json,content_type='application/json')
#end def

def registrarEstudiante(request):
	service = ActividadService.get_instance()
	resp = service.addEstudiante(request)
	if resp[0]:
		return HttpResponse(resp[1], content_type='application/json')
	#end if
	return render(request,'actividades/addEstudiante.html',{'formU':resp[1],'form':resp[2]})
#end if

def registrarDocente(request):
	service = ActividadService.get_instance()
	resp = service.addDocente(request)
	if resp[0]:
		return HttpResponse(resp[1], content_type='application/json')
	#end if
	return render(request,'actividades/addDocente.html',{'formU':resp[1],'form':resp[2]})
#end if	

def registrarJefe(request):
	service = ActividadService.get_instance()
	resp = service.addJefe(request)
	if resp[0]:
		return HttpResponse(resp[1], content_type='application/json')
	#end if
	return render(request,'actividades/addJefe.html',{'formU':resp[1],'form':resp[2]})
#end if	

def registrarActividad(request):
	service = ActividadService.get_instance()
	resp = service.addActividad(request)
	if resp[0]:
		return HttpResponse(resp[1], content_type='application/json')
	#end if
	url = "/actividad/add/actividad/"
	return render(request, 'actividades/addActividad.html',{'formA':resp[1],'formF':resp[2],'formS':resp[3],'formD':resp[4], 'url':url})
#end if

@login_required(login_url=LOGIN_URL)
def editarActividad(request,id):
	service = ActividadService.get_instance()
	actividad = Actividad.objects.filter(id=id)
	if actividad:
		resp = service.editActividad(request,actividad[0])
		if resp[0]:
			return HttpResponse(resp[1], content_type='application/json')
		#end if
		url = "/actividad/edit/actividad/%d/"%(int(id))
		return render(request, 'actividades/addActividad.html',{'formA':resp[1],'formF':resp[2],'formS':resp[3],'formD':resp[4], 'url':url})
	#end if
	return render(request,'actividades/404.html',{'mensaje':"No existe una actividad con esa id"})
#end if

@csrf_exempt
def validUser(request):
    username = request.POST.get('username',False)
    if username:
        user = User.objects.filter(username=username)
        if not user: 
            return HttpResponse('true',content_type='application/json')
        return HttpResponse('false',content_type='application/json')
        #end def 
    #end def
    return HttpResponse('false',content_type='application/json')
#end def 

@csrf_exempt
def validEmail(request):
    email = request.POST.get('email',False)
    if email:
        user = User.objects.filter(email=email)
        if not user: 
            return HttpResponse('true',content_type='application/json')
        return HttpResponse('false',content_type='application/json')
        #end def 
    #end def
    return HttpResponse('false',content_type='application/json')
#end def

@login_required(login_url=LOGIN_URL)
def singleActividad(request, id):
	actividad = Actividad.objects.filter(id=id).first()
	if actividad:
		foto = Foto.objects.filter(actividad=actividad)
		documento = Documento.objects.filter(actividad=actividad)
		soporte = Soporte.objects.filter(actividad=actividad)
		return render(request,'actividades/singleActividad.html',{'actividad':actividad, 'foto':foto, 'documento':documento, 'soporte':soporte})
	#end if
	return render(request,'actividades/404.html',{'mensaje':"No existe una actividad con esa id"})
#end def

@login_required(login_url=LOGIN_URL)
def estadisticas(request):
	anio = Actividad.objects.filter(estado=True).distinct('anio')
	return render(request,'actividades/estadisticas.html',{'anio':anio})
#end def

@csrf_exempt
def wsEstadisticas(request):
	service = ActividadService.get_instance()
	estadistica = service.estadisticaActividad(request)
	if estadistica:
		return HttpResponse(estadistica,content_type="application/json")
	#end if
	return HttpResponse([],content_type="application/json")
#end def

@csrf_exempt
def filtroAB(request):
	service = ActividadService.get_instance()
	estadistica = service.filtroAB(request)
	if estadistica:
		return HttpResponse(estadistica,content_type="application/json")
	#end if
	return HttpResponse([],content_type="application/json")
#end def

@csrf_exempt
def filtroAP(request):
	service = ActividadService.get_instance()
	estadistica = service.filtroAP(request)
	if estadistica:
		return HttpResponse(estadistica,content_type="application/json")
	#end if
	return HttpResponse([],content_type="application/json")
#end def 