# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacionTurnos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horariotrabajo',
            name='dia',
            field=models.IntegerField(default=0, choices=[(1, b'Lunes'), (2, b'Martes'), (3, b'Miercoles'), (4, b'Jueves'), (5, b'Viernes'), (6, b'Sabado'), (0, b'Domingo')]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='numeroObraSocial',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
