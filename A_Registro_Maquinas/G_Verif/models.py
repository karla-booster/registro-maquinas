from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Verif(models.Model):
    verf = models.CharField(max_length=100, verbose_name='Verificacion:')
    contador= models.IntegerField(verbose_name='Repeticion por turno:')

    class Meta:
        verbose_name = 'Verificacion'
        verbose_name_plural = 'Verificaciones'

    def __str__(self):
        return self.verf

class Aut(models.Model):
    verf = models.CharField(max_length=100, verbose_name='Verificacion:')
    contador= models.IntegerField(verbose_name='Repeticion por turno:')

    class Meta:
        verbose_name = 'Verificacion'
        verbose_name_plural = 'Verificaciones'

    def __str__(self):
        return self.verf