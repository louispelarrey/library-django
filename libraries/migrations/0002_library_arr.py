# Generated by Django 3.2.16 on 2023-01-06 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='arr',
            field=models.CharField(blank=True, max_length=255, verbose_name='Arrondissement'),
        ),
    ]
