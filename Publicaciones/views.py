# Create your views here.
# Developed with class based views
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.views.generic.base import View
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Usuarios.models import *
from Publicaciones.forms import ContactoForm
from django.contrib.auth.models import User
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.core.mail import send_mail



# Publicaciones
# List of User-Publications

def ImageUser(id):
    image = Usuario.objects.get(username = id).avatar
    return image

class UserPulicationsView(View):
    template_name='Publicaciones/Userpub.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):

        listPU = Publicacion.objects.filter(UserPub = request.user).order_by('title')
        return render(request, self.template_name, {'listPU':listPU,'image':ImageUser(request.user)})

#Public InitUser
class PublicationsView(View):
    template_name='Publicaciones/public.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        list = Publicacion.objects.all().order_by('-date')
        return render(request, self.template_name, {'list':list,'image':ImageUser(request.user)})

#Public Init
class PublicationsViewPublic(View):
    template_name='Publicaciones/public.html'

    def get(self, request, *args, **kwargs):
        list = Publicacion.objects.all().order_by('-date')
        return render(request, self.template_name, {'list':list})


# Publications details
#Average Points
def AveragePoints(id):
    sum = 0
    for i in Comentarios.objects.filter(id_Pub=id): sum = sum + i.Points
    c = Comentarios.objects.filter(id_Pub=id).count()
    average = 5
    if sum>0: average = sum/c
    return average

class PublicationView(View):
    template_name='Publicaciones/Publication.html'
    form_class = CommentForm

    @method_decorator(login_required)
    def get(self, request, *arg, **kwargs):
        id = self.kwargs['Publication_id']
        publicacion = get_object_or_404(Publicacion, pk=id)
        formC = self.form_class()
        av=AveragePoints(id)
        comentarios = Comentarios.objects.filter(id_Pub = id)
        return render(request,self.template_name,{'image':ImageUser(request.user),'publication':publicacion, 'comments':comentarios, 'user':request.user, 'formC': formC, 'av':av})

#New Comment
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):

        id = self.kwargs['Publication_id']
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():    
            form.save()
            return redirect('/Publicaciones/'+id)

        return render(request, self.template_name, {'form': form})


class AddPublicationView(View):
    form_class = PublicationForm
    template_name = 'Publicaciones/newPublication.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        formP = self.form_class()
	b = Board.objects.all().count()
        return render(request, self.template_name, {'b':b,'formP': formP, 'user':request.user, 'image':ImageUser(request.user)})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():    
            form.save()
            return redirect('/Publicaciones')

        return render(request, self.template_name, {'formP': form})

# Edit Publication
class EditPublicationView(View):
    form_class = PublicationForm
    template_name = 'Publicaciones/editPublications.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditPublicationView, self).dispatch(*args, **kwargs)

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        id = self.kwargs['publication_id']
        publicacion = get_object_or_404(Publicacion, pk=id)
        formP = self.form_class(instance = publicacion)
        return render(request, self.template_name, {'pub':publicacion,'formP': formP,'image':ImageUser(request.user)})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        id = self.kwargs['publication_id']
        publicacion = get_object_or_404(Publicacion, pk=id)
        form = self.form_class(request.POST, request.FILES, instance=publicacion)

        if form.is_valid():
             form.save()
             return redirect('/Publicaciones/'+id)

        return render(request, self.template_name, {'form': form})

# Delete Publication
class DeletePublicationView(View): 

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        id = self.kwargs['publication_id']
        publicacion = get_object_or_404(Publicacion, pk=id)
        
        publicacion.delete()

        return redirect('/Publicaciones/')

# Delete Comments

class DeleteCommentView(View): 

    @method_decorator(login_required)

    def get(self, request, *args, **kwargs):

        id = self.kwargs['comment_id']
        comentario = get_object_or_404(Comentarios, pk=id)
        idp = self.kwargs['publication_id']
        publicacion = get_object_or_404(Publicacion, pk=idp)

        comentario.delete()

        return redirect('/Publicaciones/'+idp)


def contacto(request):
	if request.method=='POST':
		formulario = ContactoForm(request.POST)
		if formulario.is_valid():
			titulo = 'Mensaje desde la Red Social Pintorreate'
			contenido = formulario.cleaned_data['mensaje'] + "\n"
			contenido += 'Enviado por: ' + formulario.cleaned_data['correo']
			correo = send_mail(titulo, contenido, settings.EMAIL_HOST_USER,
    ['i12cemod@gmail.com'], fail_silently=False)
			return HttpResponseRedirect('/Publicaciones/')
	else:
		formulario = ContactoForm()
	return render_to_response('contactoform.html',{'formulario':formulario}, context_instance=RequestContext(request))
