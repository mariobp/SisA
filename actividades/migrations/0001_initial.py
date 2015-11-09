# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('objetivo', models.TextField(max_length=600)),
                ('anio', models.IntegerField(default=2015, verbose_name=b'A\xc3\xb1o')),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AsignacionAsi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anio', models.IntegerField(default=2015, max_length=4, verbose_name=b'A\xc3\xb1o')),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(max_length=500)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200, verbose_name=b'* Nombres')),
                ('apellidos', models.CharField(max_length=200, verbose_name=b'* Apellidos')),
                ('fecha_Nacimiento', models.DateField(verbose_name=b'* Fecha de Nacimiento')),
                ('sexo', models.BooleanField(default=True, verbose_name=b'* Sexo', choices=[(True, b'Hombre'), (False, b'Mujer')])),
                ('identificacion', models.CharField(unique=True, max_length=200, verbose_name=b'* Identificaci\xc3\xb3n')),
                ('telefono', models.IntegerField(max_length=50, verbose_name=b'* Telefono')),
                ('direcion', models.CharField(max_length=400, verbose_name=b'* Direcci\xc3\xb3n')),
                ('estado', models.BooleanField(default=True)),
                ('codigo', models.IntegerField(unique=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'ordering': ['nombre'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('archivo', models.FileField(null=True, upload_to=b'actividad/documentos', blank=True)),
                ('actividad', models.ForeignKey(to='actividades.Actividad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200, verbose_name=b'* Nombres')),
                ('apellidos', models.CharField(max_length=200, verbose_name=b'* Apellidos')),
                ('fecha_Nacimiento', models.DateField(verbose_name=b'* Fecha de Nacimiento')),
                ('sexo', models.BooleanField(default=True, verbose_name=b'* Sexo', choices=[(True, b'Hombre'), (False, b'Mujer')])),
                ('identificacion', models.CharField(unique=True, max_length=200, verbose_name=b'* Identificaci\xc3\xb3n')),
                ('telefono', models.IntegerField(max_length=50, verbose_name=b'* Telefono')),
                ('direcion', models.CharField(max_length=400, verbose_name=b'* Direcci\xc3\xb3n')),
                ('estado', models.BooleanField(default=True)),
                ('codigo', models.IntegerField(unique=True)),
            ],
            options={
                'ordering': ['nombre'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(null=True, upload_to=b'actividad/fotos', blank=True)),
                ('actividad', models.ForeignKey(to='actividades.Actividad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JefeDepartamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200, verbose_name=b'* Nombres')),
                ('apellidos', models.CharField(max_length=200, verbose_name=b'* Apellidos')),
                ('fecha_Nacimiento', models.DateField(verbose_name=b'* Fecha de Nacimiento')),
                ('sexo', models.BooleanField(default=True, verbose_name=b'* Sexo', choices=[(True, b'Hombre'), (False, b'Mujer')])),
                ('identificacion', models.CharField(unique=True, max_length=200, verbose_name=b'* Identificaci\xc3\xb3n')),
                ('telefono', models.IntegerField(max_length=50, verbose_name=b'* Telefono')),
                ('direcion', models.CharField(max_length=400, verbose_name=b'* Direcci\xc3\xb3n')),
                ('estado', models.BooleanField(default=True)),
                ('codigo', models.IntegerField(unique=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'ordering': ['nombre'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlanEstudio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProgAcademica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('periodo', models.IntegerField(choices=[(1, b'Primer Periodo'), (2, b'Segundo Periodo')])),
                ('anio', models.IntegerField(default=2015, verbose_name=b'A\xc3\xb1o')),
                ('asignatura', models.ForeignKey(to='actividades.Asignatura')),
                ('planestudio', models.ForeignKey(verbose_name=b'Plan de Estudio', to='actividades.PlanEstudio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(max_length=500)),
                ('estado', models.BooleanField(default=True)),
                ('facultad', models.ForeignKey(to='actividades.Facultad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('periodo', models.IntegerField(choices=[(1, b'Primer Periodo'), (2, b'Segundo Periodo')])),
                ('anio', models.IntegerField(default=2015, max_length=4, verbose_name=b'A\xc3\xb1o')),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Soporte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('archivo', models.FileField(null=True, upload_to=b'actividad/soportes', blank=True)),
                ('actividad', models.ForeignKey(to='actividades.Actividad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(max_length=600)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='planestudio',
            name='programa',
            field=models.ForeignKey(to='actividades.Programa'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='facultad',
            name='sede',
            field=models.ForeignKey(to='actividades.Sede'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiante',
            name='programa',
            field=models.ForeignKey(to='actividades.Programa'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiante',
            name='semestre',
            field=models.ForeignKey(to='actividades.Semestre'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiante',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asignacionasi',
            name='docente',
            field=models.ForeignKey(to='actividades.Docente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asignacionasi',
            name='estudiantes',
            field=models.ManyToManyField(to='actividades.Estudiante'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asignacionasi',
            name='progacademica',
            field=models.ForeignKey(verbose_name=b'Programac\xc3\xb3n Academica', to='actividades.ProgAcademica'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actividad',
            name='asignatura',
            field=models.ManyToManyField(to='actividades.AsignacionAsi'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actividad',
            name='jefe',
            field=models.ForeignKey(to='actividades.JefeDepartamento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actividad',
            name='tipo',
            field=models.ForeignKey(to='actividades.Tipo'),
            preserve_default=True,
        ),
    ]
