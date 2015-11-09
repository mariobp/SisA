from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SisA.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^actividad/', include('actividades.urls'))
)

urlpatterns += patterns('SisA.views',
    url(r'^$', 'index_view', name='vista_principal'),
    url(r'^login/','login_view',name='login'),
	url(r'^logout/','logout_view',name='logout')		
	)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),       
)