# Generated by Django 4.0.4 on 2022-05-31 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_familiares', '0003_alter_app_familiares_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]