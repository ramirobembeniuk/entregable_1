# Generated by Django 4.0.4 on 2022-05-25 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App_Familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('observaciones', models.CharField(blank=True, max_length=200, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
