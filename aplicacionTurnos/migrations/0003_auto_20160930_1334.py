# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacionTurnos', '0002_auto_20160829_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tratamiento',
            name='duracion',
            field=models.TimeField(default=datetime.datetime(2016, 9, 30, 0, 0)),
        ),
    ]
