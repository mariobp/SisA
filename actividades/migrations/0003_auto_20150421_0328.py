# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0002_auto_20150419_1515'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asignacionasi',
            options={'verbose_name': 'Asignaci\xf3n de Asignatura', 'verbose_name_plural': 'Asinaciones de Asignatura'},
        ),
        migrations.AlterModelOptions(
            name='facultad',
            options={'verbose_name': 'Facultad', 'verbose_name_plural': 'Facultades'},
        ),
        migrations.AlterModelOptions(
            name='jefedepartamento',
            options={'verbose_name': 'Jefe de Departamento', 'verbose_name_plural': 'Jefes de Departamento'},
        ),
        migrations.AlterModelOptions(
            name='planestudio',
            options={'verbose_name': 'Plan de Estudio', 'verbose_name_plural': 'Plan de Estudios'},
        ),
        migrations.AlterModelOptions(
            name='progacademica',
            options={'verbose_name': 'Programac\xf3n Acedemica', 'verbose_name_plural': 'Programaciones Acedemicas'},
        ),
        migrations.AddField(
            model_name='actividad',
            name='periodo',
            field=models.IntegerField(default=1, choices=[(1, b'Primer Periodo'), (2, b'Segundo Periodo')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='codigo',
            field=models.IntegerField(unique=True, verbose_name=b'* Codigo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='programa',
            field=models.ForeignKey(verbose_name=b'* Programa', to='actividades.Programa'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='semestre',
            field=models.ForeignKey(verbose_name=b'* Semestre', to='actividades.Semestre'),
            preserve_default=True,
        ),
    ]
