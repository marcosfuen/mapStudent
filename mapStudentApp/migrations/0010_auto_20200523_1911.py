# Generated by Django 3.0.6 on 2020-05-23 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapStudentApp', '0009_auto_20200523_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuesta',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Nombre y Apellidos'),
        ),
        migrations.AlterField(
            model_name='studentinformation',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Nombre y Apellidos'),
        ),
    ]
