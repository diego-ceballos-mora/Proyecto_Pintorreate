#encoding: utf-8

from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User

class BoardForm(forms.ModelForm):
	class Meta:
		model = Board

	def __int__(self,*args, **kargs):
		super(BoardForm, self).__init__(*args, **Kwargs)
		fields=('name','userBoard','description')