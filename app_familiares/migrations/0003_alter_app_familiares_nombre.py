# Generated by Django 4.0.4 on 2022-05-31 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_familiares', '0002_alter_app_familiares_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app_familiares',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
