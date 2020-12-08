# Generated by Django 3.1.2 on 2020-12-07 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32)),
                ('apellido', models.CharField(max_length=32)),
                ('fecha_nac', models.DateField()),
                ('edad', models.IntegerField()),
                ('direccion', models.CharField(max_length=64)),
                ('observaciones', models.CharField(blank=True, max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_finalizacion', models.DateField()),
                ('contenido', models.CharField(max_length=512)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('monto', models.IntegerField()),
                ('Alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nombre_instructor', to='gestion.alumno')),
            ],
        ),
        migrations.CreateModel(
            name='PadreAlumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32)),
                ('apellido', models.CharField(max_length=32)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=64)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='padre_alumno', to='gestion.alumno')),
            ],
        ),
        migrations.CreateModel(
            name='MadreAlumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32)),
                ('apellido', models.CharField(max_length=32)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=64)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='madre_alumno', to='gestion.alumno')),
            ],
        ),
    ]
