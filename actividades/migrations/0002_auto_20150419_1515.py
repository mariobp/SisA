# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semestre',
            name='anio',
        ),
        migrations.RemoveField(
            model_name='semestre',
            name='periodo',
        ),
    ]
