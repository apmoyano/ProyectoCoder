# Generated by Django 4.0.3 on 2022-03-29 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0005_alter_viajes_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viajes',
            name='id',
        ),
        migrations.AlterField(
            model_name='viajes',
            name='pais',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
