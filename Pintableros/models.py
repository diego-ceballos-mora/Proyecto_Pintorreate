from django.db import models
from django.utils.encoding import smart_unicode
from datetime import date
from Usuarios.models import Usuario

class Board(models.Model):
	name=models.CharField(max_length=100,unique= True)
	userBoard=models.ForeignKey(Usuario, related_name='FK_User_Board')
	description=models.CharField(max_length=300, blank=True)
	date=models.DateTimeField(auto_now_add = True)


	def __unicode__(self):
		return self.name
