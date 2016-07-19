from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
class Categoria(models.Model):
	nameCat=models.CharField(max_length=100,unique= True)
	descriptionCat=models.CharField(max_length=300, blank=True)
	imageCat=models.ImageField(upload_to = 'Categorias', verbose_name='Picture')

	def __unicode__(self):
		return self.nameCat
