from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from .views import *
from Publicaciones.views import PublicationView


urlpatterns = patterns('',
	url(r'^$', ListCategoryView.as_view(), name='list'),
	url(r'^categories$', ListCategoryView.as_view(), name='categories'),
	url(r'^category$', CategoryView.as_view(), name='detail'),
	url(r'^(?P<Category_id>\d+)$', CategoryView.as_view(), name='detail'),
)
