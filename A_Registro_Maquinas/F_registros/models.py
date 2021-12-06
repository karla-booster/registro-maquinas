from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Registros(models.Model):
    maquina= models.CharField(max_length=100, verbose_name="maquina", editable=False)
    area= models.CharField(max_length=10,verbose_name="área", editable=False)
    id_estado=models.IntegerField(editable=False, verbose_name='id_estado', default=0)
    estado= models.CharField(max_length=100, verbose_name="estado", editable=False)
    usuario= models.IntegerField(editable=False, verbose_name='Usuario', null=True)
    departamento = models.CharField(max_length=100, verbose_name="área", editable=False)
    created_at= models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Creado:')
    active= models.BooleanField(verbose_name='¿Activa?', editable=False)
    cambio= models.DateTimeField(auto_now=True, editable=False, verbose_name='Cambio:')
    comment= models.CharField(max_length=200, verbose_name="comentario", editable=False, null=True)

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'

    def __str__(self):
        return self.maquina