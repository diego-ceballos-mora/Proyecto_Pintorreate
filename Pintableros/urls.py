from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from .views import *


urlpatterns = patterns('',
	url(r'^$', ListBoardView.as_view(), name='list'),
	url(r'^Pintableros$', ListBoardView.as_view(), name='boards'),
	url(r'^board$', BoardView.as_view(), name='detail'),
	url(r'^(?P<board_id>\d+)$', BoardView.as_view(), name='detail'),

	url(r'^newB$', AddBoardView.as_view(), name='addPub'),
	url(r'^editB/(?P<board_id>\d+)$', EditBoardView.as_view(), name='editPub'),
	url(r'^deleteB/(?P<board_id>\d+)$', DeleteBoardView.as_view(), name='deletePub'),
)
