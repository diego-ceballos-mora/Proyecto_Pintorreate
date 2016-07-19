# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from forms import UserCreationForm, MyUserForm
from django.contrib.auth import login, authenticate, logout

# Developed with class based views
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Usuarios.models import *


#User Image
def ImageUser(id):
    image = Usuario.objects.get(username = id).avatar
    return image


#View User
@login_required(login_url='/Usuarios/login')
def ViewProfile(request, user_id):

    u = Usuario.objects.get(id = user_id)
    context = {'profile': request.user, 'u':u, 'image':ImageUser(request.user)}
    return render(request, 'Usuarios/viewuser.html', context)


# New User
def Register(request):
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        # form = UserCreationForm()
        form = MyUserForm()
    context = {'form':form}
    return render(request, 'Usuarios/newuser.html',  context)

def userList(request):
    list = Usuario.objects.all().order_by('last_name')
    context = {'userList': list}
    return render(request, 'users/userslist.html', context)


#Modificate User
@login_required(login_url='/Usuarios/login')
def MofidUser(request):
    user = get_object_or_404(Usuario, pk= request.user)
    if request.method == 'POST':
        form = EditUserForm(request.POST, request.FILES, instance = user)
        if form.is_valid():
            form.save()
            return redirect('/Publicaciones/public.html')
    else:
        form = EditUserForm(instance = user)
    context = {'form':form,'image':ImageUser(request.user)}
    return render(request, 'Usuarios/moduser.html',context)


#Delete User
def userDelete(request, userphoto_id):
	if (request.user.is_superuser and request.user.is_staff):
		user = get_object_or_404(Usuario, pk = user_id)
		user.delete()
		return redirect('/Usuarios/list')

