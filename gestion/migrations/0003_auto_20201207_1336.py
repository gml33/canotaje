# Generated by Django 3.1.2 on 2020-12-07 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_auto_20201207_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='contenido',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
    ]
