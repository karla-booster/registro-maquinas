from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class pp(models.Model):
    maquina= models.CharField(max_length=100, verbose_name="Maquina", editable=False)
    orden= models.IntegerField(verbose_name="Orden", editable=False)
    noparte= models.CharField(max_length=100, verbose_name="NumeroParte", editable=False)
    qty = models.IntegerField(verbose_name="Qty", editable=False)
    fecha= models.DateField(editable=False, verbose_name='Fecha')

    class Meta:
        verbose_name = 'PlanP'
        verbose_name_plural = 'PlanP'

    def __str__(self):
        return self.orden

class RegProd(models.Model):
    maquina= models.CharField(max_length=100, verbose_name="maquina", editable=False)
    area= models.CharField(max_length=10,verbose_name="área", editable=False)
    orden= models.IntegerField(verbose_name="orden", editable=False)
    noparte = models.CharField(max_length=100, verbose_name="noparte", editable=False)
    qtyprod= models.IntegerField(verbose_name="QtyProd", editable=False)
    active= models.BooleanField(verbose_name='¿Activa?', editable=False)
    created_at= models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Creado:')
    usuario= models.IntegerField(editable=False, verbose_name='Usuario')

    class Meta:
        verbose_name = 'Registro Produccion'
        verbose_name_plural = 'Registros Produccion'

    def __str__(self):
        return self.orden

class CambioOrden(models.Model):
    maquina= models.CharField(max_length=100, verbose_name="Maquina", editable=False)
    orden= models.IntegerField(verbose_name="Orden", editable=False)
    noparte= models.CharField(max_length=100, verbose_name="NumeroParte", editable=False)
    modelo= models.IntegerField(editable=False, verbose_name='Modelo')
    qty = models.IntegerField(verbose_name="Qty", editable=False)
    fecha= models.DateField(editable=False, verbose_name='Fecha de orden')
    active= models.BooleanField(editable=False, default=False)
    reci= models.IntegerField(editable=False, verbose_name='Piezas Recibidas')
    prod= models.IntegerField(editable=False, verbose_name='Piezas Producidas')
    rech= models.IntegerField(editable=False, verbose_name='Piezas Rechazadas')
    rr= models.IntegerField(editable=False, verbose_name='Numero RR')
    totalacep= models.IntegerField(editable=False, verbose_name='Total piezas aceptadas')
    created_at= models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Creado:')
    updated_at= models.DateTimeField(auto_now=True, editable=False, verbose_name='Cambio:')

    class Meta:
        verbose_name = 'Cambio Orden'
        verbose_name_plural = 'Cambio Ordenes'

    def __str__(self):
        return self.orden
