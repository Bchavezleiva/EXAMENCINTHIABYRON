# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-24 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese el nombre del cliente: ', max_length=50)),
                ('telefono', models.CharField(help_text='Ingrese el numero de telefono: ', max_length=10)),
                ('sexo', models.CharField(help_text='Ingrese el sexo: ', max_length=1)),
                ('fecha', models.DateField(help_text='Ingrese la fecha de nacimiento: ')),
            ],
        ),
    ]
