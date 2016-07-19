#encoding: utf-8

from django.http import HttpResponse

from django.forms import ModelForm 
from django import forms
from .models import *


class PublicationForm(ModelForm):
	class Meta:
		model = Publicacion

	def __int__(self,*args, **kargs):
		super(PublicationForm, self).__init__(*args, **Kwargs)
		self.fields['title'].label = 'Título de la Publicación:'
		self.fields['imagePub'].label = 'Imagen De la Publicación:'
		self.fields['descriptionPub'].label = 'Descripción corta(300 Caracteres):'
		self.fields['CatPub'].label = 'Elija Categoría:'
		self.fields['boardPub'].label = 'Elija un tablón para la Publicación:'

class CommentForm(ModelForm):
	class Meta:
		model = Comentarios

	def __int__(self,*args, **kargs):
		super(CommentForm, self).__init__(*args, **Kwargs)
		self.fields['descriptionCom'].label = 'Comentario:'
		self.fields['Points'].label = 'Puntuacion:'
		

class ContactoForm(forms.Form):
	correo = forms.EmailField(label='Tu Email')
	mensaje = forms.CharField(widget=forms.Textarea)
