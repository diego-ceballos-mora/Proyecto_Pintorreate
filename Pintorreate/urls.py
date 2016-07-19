from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from Pintorreate import views
from .views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Index
    url(r'^$index', TemplateView.as_view(template_name='index.html'), name='index'),

    # Login
    url(r'^$', views.userLogin, name='login'),

    #logout
    url(r'^logout$', views.userLogout, name='logout'),

    #Usuario app
    url(r'^Usuarios/', include ('Usuarios.urls', namespace='Usuarios')),

    #Publicaciones app
    url(r'^Publicaciones/', include ('Publicaciones.urls', namespace='Publicaciones')),

    #Pintableros app
    url(r'^Pintableros/', include ('Pintableros.urls', namespace='Pintableros')),

    #Categorias app
    url(r'^Categorias/', include ('Categorias.urls', namespace='Categorias')),
   


) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

