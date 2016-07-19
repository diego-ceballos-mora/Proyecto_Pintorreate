from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from Publicaciones import views
from .views import *

urlpatterns = patterns('',
	url(r'^$', UserPulicationsView.as_view(), name='listUserInitial'),
	url(r'^contactoform', 'Publicaciones.views.contacto'),
	url(r'^public', PublicationsView.as_view(), name='listInitial'),
	url(r'^Generalpublic', PublicationsViewPublic.as_view(), name='listInitialPublic'),
	url(r'^UserPublic$', UserPulicationsView.as_view(), name='listUserPublication'),
	url(r'^(?P<Publication_id>\d+)$', PublicationView.as_view(), name='detailPublication'),
	url(r'^newP$', AddPublicationView.as_view(), name='addPub'),
	url(r'^mod/(?P<publication_id>\d+)$', EditPublicationView.as_view(), name='editPub'),
	url(r'^delete/(?P<publication_id>\d+)$', DeletePublicationView.as_view(), name='deletePub'),
	url(r'^deleteC/(?P<comment_id>\d+)/pub/(?P<publication_id>\d+)$', DeleteCommentView.as_view(), name='deleteComment'),
)
