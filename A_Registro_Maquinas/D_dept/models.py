from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Dept(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return self.name
