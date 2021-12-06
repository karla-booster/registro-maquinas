from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from D_dept.models import Dept

# Create your models here.

class Estados(models.Model):
    estado = models.CharField(max_length=100, verbose_name='Estado')
    departamento = models.ManyToManyField(Dept, verbose_name='Departamento', related_name="dept")
    colorfondo = models.CharField(max_length=100, verbose_name='Color de fondo', default='white')
    colorletra = models.CharField(max_length=100, verbose_name='Color de letra', default='black')
    nivel = models.IntegerField(verbose_name='Nivel', default=3)

    class Meta:
        verbose_name = 'Estado Disponible'
        verbose_name_plural = 'Estados Disponibles'

    def __str__(self):
        return self.estado

