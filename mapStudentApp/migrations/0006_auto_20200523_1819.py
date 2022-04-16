# Generated by Django 3.0.6 on 2020-05-23 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapStudentApp', '0005_incidencias_startdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinformation',
            name='municipality',
        ),
        migrations.AddField(
            model_name='studentinformation',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Dirección'),
        ),
    ]
