# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HorarioTrabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.IntegerField(default=0, max_length=1, choices=[(1, b'Lunes'), (2, b'Martes'), (3, b'Miercoles'), (4, b'Jueves'), (5, b'Viernes'), (6, b'Sabado'), (0, b'Domingo')])),
                ('horaInicio', models.TimeField()),
                ('horaFin', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HorarioTurno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.DateField()),
                ('horaInicio', models.TimeField()),
                ('horaFin', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('dni', models.IntegerField()),
                ('telefono', models.IntegerField(blank=True)),
                ('correo', models.CharField(max_length=100, blank=True)),
                ('especialidad', models.ForeignKey(to='aplicacionTurnos.Especialidad')),
                ('horario', models.ForeignKey(to='aplicacionTurnos.HorarioTrabajo')),
            ],
        ),
        migrations.CreateModel(
            name='ObraSocial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('dni', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('fechaNacimiento', models.DateField()),
                ('numeroObraSocial', models.IntegerField(blank=True)),
                ('obraSocial', models.ForeignKey(to='aplicacionTurnos.ObraSocial')),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('duracion', models.TimeField(default=datetime.datetime(2016, 8, 29, 0, 0))),
                ('precio', models.IntegerField(default=0, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(default=b'Pend', max_length=4, choices=[(b'Pend', b'Pendiente'), (b'Aten', b'Atendido'), (b'CM', b'Cancelado por Medico'), (b'CP', b'Cancelado por Paciente'), (b'Ause', b'Ausente')])),
                ('horario', models.ForeignKey(to='aplicacionTurnos.HorarioTurno')),
                ('medico', models.ForeignKey(to='aplicacionTurnos.Medico')),
                ('paciente', models.ForeignKey(to='aplicacionTurnos.Paciente')),
                ('tratamiento', models.ForeignKey(to='aplicacionTurnos.Tratamiento')),
            ],
        ),
    ]
