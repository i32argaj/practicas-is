from django.conf.urls import patterns, include, url
from django.contrib import admin
from liga import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ligaFutbol.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^clasificacion/', include('liga.urls')),
    url(r'^partidos/', include('calendario.urls')),
    url(r'^usuario/registro$', 'usuario.views.signup', name='signup'),
    url(r'^usuario/login$', login, {'template_name': 'login.html', }, name="login"),
    url(r'^usuario/logout$', logout, {'template_name': 'home.html', }, name="logout"),
    url(r'^$', include('home.urls')),
    url(r'^crearEquipo/','liga.views.crearEquipo',name='crearEquipo'),
    url(r'^modificarEquipo/(?P<nombreEquipo>\D+)/$','liga.views.modificarEquipo',name='modificarEquipo'),
)+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
