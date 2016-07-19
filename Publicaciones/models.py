from django.db import models
from django.utils.encoding import smart_unicode
from datetime import date
from Usuarios.models import Usuario
from Categorias.models import Categoria
from Pintableros.models import *


class Publicacion(models.Model):
	title=models.CharField(max_length=50,unique=True)
	imagePub=models.ImageField(upload_to = 'Publicaciones', blank=True)
	descriptionPub=models.TextField(max_length=300, blank=True)
	date=models.DateTimeField(auto_now_add = True)
	boardPub=models.ForeignKey(Board, related_name='FK_Board_Pub', blank=True, default="Ninguno")	
	UserPub=models.ForeignKey(Usuario, related_name='FK_User_Pub')
	CatPub=models.ForeignKey(Categoria,related_name = 'FK_Cat_Pub')

	def __unicode__(self):
		return u'%s %s' % (self.title, self.UserPub)

CHOICES = [(i,i) for i in range(11)]

class Comentarios(models.Model):
	id_User=models.ForeignKey(Usuario,related_name='FK_User_Com')
	descriptionCom=models.TextField(max_length=180)
	Points=models.IntegerField(default=0,choices=CHOICES)
	date=models.DateTimeField(auto_now_add = True)
	id_Pub=models.ForeignKey(Publicacion,related_name='FK_Com_Pub')

	def __unicode__(self):
		return u'%s %s %s' % (self.id_User, self.Points, self.id_Pub)
