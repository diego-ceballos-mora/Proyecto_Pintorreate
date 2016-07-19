from django.conf.urls import patterns, include, url

from Usuarios import views

urlpatterns = patterns('',
    # Users
    url(r'^list$', views.userList, name='list'),
    url(r'^new$', views.Register, name='new'),
    url(r'^profile$', views.MofidUser, name='mod'),
    url(r'^delete/(?P<user_id>\d+)$', views.userDelete, name='delete'),
)
