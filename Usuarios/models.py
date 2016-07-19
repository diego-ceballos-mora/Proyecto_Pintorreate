from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode
from datetime import date


# Create your models here.
class Usuario(User):
	avatar = models.ImageField(upload_to = 'avatar', blank = True)

	

		
