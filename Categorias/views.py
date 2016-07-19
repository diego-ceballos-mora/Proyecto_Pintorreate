# Create your views here.
# Developed with class based views
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Publicaciones.models import *


def ImageUser(id):
    image = Usuario.objects.get(username = id).avatar
    return image

# Categories details
class CategoryView(View):
	template_name='Publicaciones/Catepub.html'

	def get(self, request, *arg, **kwargs):
		id = self.kwargs['Category_id']

		listPC = Categoria.objects.get(id=id).FK_Cat_Pub.all()
		categoria = Categoria.objects.get(id=id).nameCat
		return render(request,self.template_name,{'category':categoria, 'listPC':listPC,'image':ImageUser(request.user)})


# List of Category
class ListCategoryView(View):
	template_name='Categorias/categories.html'

	def get(self, request, *args, **kwargs):
		list = Categoria.objects.all().order_by('nameCat')
		return render(request, self.template_name, {'list':list,'image':ImageUser(request.user)})
