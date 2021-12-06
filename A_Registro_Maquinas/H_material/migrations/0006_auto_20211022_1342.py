# Generated by Django 3.2.7 on 2021-10-22 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('H_material', '0005_alter_regprod_noparte'),
    ]

    operations = [
        migrations.CreateModel(
            name='CambioOrden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maquina', models.CharField(editable=False, max_length=100, verbose_name='Maquina')),
                ('orden', models.IntegerField(editable=False, verbose_name='Orden')),
                ('noparte', models.CharField(editable=False, max_length=100, verbose_name='NumeroParte')),
                ('modelo', models.IntegerField(editable=False, verbose_name='Modelo')),
                ('qty', models.IntegerField(editable=False, verbose_name='Qty')),
                ('fecha', models.DateField(editable=False, verbose_name='Fecha de orden')),
                ('active', models.BooleanField(default=False, editable=False)),
                ('reci', models.IntegerField(editable=False, verbose_name='Piezas Recibidas')),
                ('prod', models.IntegerField(editable=False, verbose_name='Piezas Producidas')),
                ('rech', models.IntegerField(editable=False, verbose_name='Piezas Rechazadas')),
                ('rr', models.IntegerField(editable=False, verbose_name='Numero RR')),
                ('totalacep', models.IntegerField(editable=False, verbose_name='Total piezas aceptadas')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado:')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Cambio:')),
            ],
            options={
                'verbose_name': 'Cambio Orden',
                'verbose_name_plural': 'Cambio Ordenes',
            },
        ),
        migrations.RemoveField(
            model_name='pp',
            name='active',
        ),
        migrations.RemoveField(
            model_name='pp',
            name='modelo',
        ),
    ]