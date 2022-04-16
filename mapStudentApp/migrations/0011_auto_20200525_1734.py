# Generated by Django 3.0.6 on 2020-05-25 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapStudentApp', '0010_auto_20200523_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='zona',
            name='cantEstudLocal',
            field=models.BigIntegerField(blank=True, default=0, null=True, verbose_name='Cant. Estudiantes localizados'),
        ),
        migrations.AddField(
            model_name='zona',
            name='cantEstudParte',
            field=models.BigIntegerField(blank=True, default=0, null=True, verbose_name='Cant. Estudiantes que dieron parte'),
        ),
        migrations.AddField(
            model_name='zona',
            name='coordinador',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre(s) y Apellido(s)'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='saf',
            field=models.BooleanField(default=True, verbose_name='Recibe atención del SAF para obtener los alimentos'),
        ),
        migrations.AlterField(
            model_name='resumen',
            name='totalEnc',
            field=models.BigIntegerField(default=0, verbose_name='Cant. de adultos mayores visitados'),
        ),
    ]