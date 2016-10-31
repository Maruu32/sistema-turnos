# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacionTurnos', '0003_auto_20160930_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tratamiento',
            name='duracion',
            field=models.TimeField(default=datetime.datetime(2016, 10, 6, 0, 0)),
        ),
    ]
