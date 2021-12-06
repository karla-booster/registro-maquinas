from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Area(models.Model):
    name = models.CharField(max_length=100, verbose_name='Área')

    class Meta:
        verbose_name = 'Área'
        verbose_name_plural = 'Áreas'

    def __str__(self):
        return self.name


class Maquina(models.Model):
    title = models.CharField(max_length=150, verbose_name='Maquina')
    area = models.ManyToManyField(Area, verbose_name='Área', blank=True, related_name="area")
    public = models.BooleanField(verbose_name='¿Activa?')

    class Meta:
        verbose_name = 'Máquina'
        verbose_name_plural = 'Máquinas'

    def __str__(self):
        return self.title