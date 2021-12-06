# Generated by Django 3.2.7 on 2021-10-05 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('D_dept', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=100, verbose_name='Estado')),
                ('departamento', models.ManyToManyField(related_name='dept', to='D_dept.Dept', verbose_name='Departamento')),
            ],
            options={
                'verbose_name': 'Estado Disponible',
                'verbose_name_plural': 'Estados Disponibles',
            },
        ),
    ]
