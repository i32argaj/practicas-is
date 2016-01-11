from django.conf.urls import url, include, patterns
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', views.mostrarCalendario, name='mostrarCalendario'),
    url(r'^(?P<numeroJornada>\d+)/$', views.mostrarJornada,name='mostrarJornada'),
)+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
