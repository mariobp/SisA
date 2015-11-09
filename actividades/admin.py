#encoding:utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from actividades.models import Semestre, Sede, Facultad, Programa, Estudiante, Docente, JefeDepartamento, Asignatura, AsignacionAsi, Tipo, Actividad, Foto, Soporte, Documento, PlanEstudio, ProgAcademica
# Register your models here.

class SemestreAdmin(admin.ModelAdmin):
	list_display = ('nombre','estado')
	search_fields = ('nombre',)
#end class

class SedeAdmin(admin.ModelAdmin):
	list_display = ('nombre','estado')
	search_fields = ('nombre',)
#end class

class FacultadAdmin(admin.ModelAdmin):
	list_display = ('nombre','sede','estado')
	search_fields = ('nombre',)
	list_filter = ('sede',)
#end class	

class programaAdmin(admin.ModelAdmin):
	list_display = ('nombre','descripcion','facultad','estado')
	search_fields = ('nombre','facultad__nombre')
	list_filter = ('facultad',)
#end class

class EstudianteAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellidos','identificacion','fecha_Nacimiento','sexo','telefono','direcion','codigo','semestre','programa','estado')
	search_fields = ('nombre','apellidos','identificacion')
	list_filter = ('sexo','codigo','semestre','programa','estado')
#end class


class DocenteAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellidos','identificacion','fecha_Nacimiento','sexo','telefono','direcion','codigo','estado')
	search_fields = ('nombre','apellidos','identificacion')
	list_filter = ('sexo','codigo','estado')
#end class

class PlanEstudioAdmin(admin.ModelAdmin):
	list_display = ('nombre','programa')
	search_fields = ('nombre','programa__nombre')
#end class

class AsignaturaAdmin(admin.ModelAdmin):
	list_display = ('nombre','descripcion','estado')
	search_fields = ('nombre',)
#end class

class AsignacionAsiAdmin(admin.ModelAdmin):
	list_display = ('progacademica','docente','anio','estado')
	list_filter = ('progacademica','docente')
	filter_horizontal = ('estudiantes',)
#end class

class TipoAdmin(admin.ModelAdmin):
	list_display = ('nombre','descripcion','estado')
	search_fields = ('nombre',)
#end class

class FotoStacked(admin.StackedInline):
	model = Foto
#end class

class SoporteStacked(admin.StackedInline):
	model = Soporte
#end class

class DocumentoStacked(admin.StackedInline):
	model = Documento
#end class

class ActividadAdmin(admin.ModelAdmin):
	list_display = ('nombre','objetivo','tipo','anio','jefe','estado')
	search_fields = ('nombre',)
	list_filter = ('tipo','jefe','anio')
	filter_horizontal = ('asignatura',)
	inlines = (FotoStacked,SoporteStacked,DocumentoStacked)
#end class

class FotoAdmin(admin.ModelAdmin):
	list_display = ('actividad','imagen')
	list_filter = ('actividad',)
#end class

class ArchivoAdmin(admin.ModelAdmin):
	list_display = ('actividad','archivo')
	list_filter = ('actividad',)
#end class 

class ProgamacionAdmin(admin.ModelAdmin):
	list_filter = ('asignatura','planestudio','anio')
	search_fields = ('asignatura__nombre',)
#end class

class MyUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2','groups','is_staff')}
        ),
    )
    list_display = ('username','email','is_staff','is_active')
#end class
admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
admin.site.register(Semestre,SemestreAdmin)
admin.site.register(Sede,SedeAdmin)
admin.site.register(Facultad,FacultadAdmin)
admin.site.register(Programa,programaAdmin)
admin.site.register(Estudiante,EstudianteAdmin)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(JefeDepartamento,DocenteAdmin)
admin.site.register(PlanEstudio, PlanEstudioAdmin)
admin.site.register(Asignatura, AsignaturaAdmin)
admin.site.register(AsignacionAsi, AsignacionAsiAdmin)
admin.site.register(Tipo,TipoAdmin)
admin.site.register(Actividad,ActividadAdmin)
admin.site.register(Foto, FotoAdmin)
admin.site.register(Soporte,ArchivoAdmin)
admin.site.register(Documento, ArchivoAdmin)
admin.site.register(ProgAcademica, ProgamacionAdmin)
