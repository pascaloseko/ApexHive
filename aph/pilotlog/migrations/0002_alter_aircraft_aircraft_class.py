# Generated by Django 5.0.2 on 2024-02-17 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pilotlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='aircraft_class',
            field=models.IntegerField(null=True),
        ),
    ]
