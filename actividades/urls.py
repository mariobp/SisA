from django.conf.urls import patterns, url

urlpatterns = patterns('actividades.views',
		url(r'^$','actividades',name='actividades'),
		url(r'^add/actividad/','registrarActividad',name='actividad'),
		url(r'^edit/actividad/(?P<id>\d+)/$','editarActividad',name='editActividad'),
		url(r'^single/actividad/(?P<id>\d+)/$','singleActividad',name='singleActividad'),
		url(r'^add/estudiante/','registrarEstudiante',name='estudiante'),
		url(r'^add/docente/','registrarDocente',name='docente'),
		url(r'^add/jefe/','registrarJefe',name='jefe'),
		url(r'^ws/actividades/','wsListActividades', name="wsActividades"),
	    url(r'^ws/validar/user/','validUser', name="validUser"),
	    url(r'^ws/validar/mail/','validEmail', name="validEmail"),
	    url(r'^estadisticas/','estadisticas', name="estadisticas"),
	    url(r'^ws/estadisticas/','wsEstadisticas', name="wsEstadisticas"),
	   	url(r'^ws/estadistica/b/','filtroAB', name="filtroAB"),
	    url(r'^ws/estadistica/p/','filtroAP', name="estadisticasFP"),

	)