# Generated by Django 3.0.6 on 2020-05-25 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapStudentApp', '0012_auto_20200525_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='encuesta',
            name='moduloGob',
            field=models.BooleanField(default=True, verbose_name='Recibe Usted el modulo asignado por el gobierno'),
        ),
    ]
