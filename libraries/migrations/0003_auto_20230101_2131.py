# Generated by Django 3.2.16 on 2023-01-01 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0002_library_geom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library',
            name='address',
        ),
        migrations.RemoveField(
            model_name='library',
            name='city',
        ),
        migrations.RemoveField(
            model_name='library',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='library',
            name='statut',
        ),
    ]
