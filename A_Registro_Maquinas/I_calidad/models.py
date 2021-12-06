from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Aprobar_piezas(models.Model):
    maquina= models.CharField(max_length=100, verbose_name="Maquina", editable=False)
    area= models.CharField(max_length=100, verbose_name="Area", editable=False)
    recibida= models.BooleanField(verbose_name="Recibida", editable=False)
    aprobada= models.BooleanField(verbose_name="Aprobada", editable=False)
    rechazada= models.BooleanField(verbose_name="Rechazada", editable=False)
    updated_at= models.DateTimeField(auto_now=True, editable=False, verbose_name='Cambio:')

    class Meta:
        verbose_name = 'Aprobar'
        verbose_name_plural = 'Aprobar'

    def __str__(self):
        return self.title