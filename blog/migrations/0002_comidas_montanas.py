# Generated by Django 4.0.3 on 2022-03-31 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_comida', models.CharField(max_length=100)),
                ('pais_origen', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Montanas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=100)),
                ('dificultad', models.IntegerField()),
            ],
        ),
    ]