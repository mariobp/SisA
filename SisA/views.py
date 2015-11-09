#encoding:utf-8
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from SisA.settings import LOGIN_URL
from SisA.forms import LoginForm
from actividades.models import Estudiante, Docente, JefeDepartamento

# from django.contrib.auth.models import User

@login_required(login_url=LOGIN_URL)
def index_view(request):
    return HttpResponseRedirect('/actividad/')
#end def


def login_view(request):
    mensaje = ""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                next = request.POST['next']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username, password=password)
                if usuario is not None and usuario.is_active:
                    login(request, usuario)
                    return HttpResponseRedirect(next)
                else:
                    mensaje = "Usuario y/o Contraseña incorrectos"
                #end if
            #end if
        #end if
        next = request.REQUEST.get('next')
        form = LoginForm()
        ctx = {'form': form, 'mensaje': mensaje, 'next':next}
        return render(request,'SisA/login.html', ctx)
#end def

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
#end def

