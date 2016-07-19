# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Developed with class based views
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


#Login
def userLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            user = request.POST['username']
            passwd = request.POST['password']
            access = authenticate(username=user, password=passwd)
            if access is not None:
                if access.is_active:
                    login(request, access)
                    return redirect('/Publicaciones/public.html')
                else:
                    return render(request, 'Usuarios/inactive.html')
            else:
                return render(request, 'Usuarios/nouser.html')
    else:
        form = AuthenticationForm()
    context = {'form': form,'user1':request.user}
    return render(request,'login.html', context)

@login_required(login_url='/')
def userLogout(request):
    logout(request)
    return redirect('/')


