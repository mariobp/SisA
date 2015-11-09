# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0003_auto_20150421_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignacionasi',
            name='anio',
            field=models.IntegerField(default=2015, verbose_name=b'A\xc3\xb1o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='docente',
            name='telefono',
            field=models.IntegerField(verbose_name=b'* Telefono'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='docente',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='telefono',
            field=models.IntegerField(verbose_name=b'* Telefono'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jefedepartamento',
            name='telefono',
            field=models.IntegerField(verbose_name=b'* Telefono'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jefedepartamento',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
