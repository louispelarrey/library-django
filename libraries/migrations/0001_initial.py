# Generated by Django 3.2.16 on 2023-01-24 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djgeojson.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nom de la librairie')),
                ('description', models.TextField(blank=True, verbose_name='Description de la librairie')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('geom', djgeojson.fields.PointField(blank=True, null=True)),
                ('arr', models.CharField(blank=True, max_length=255, verbose_name='Arrondissement')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Librairie',
                'verbose_name_plural': 'Librairies',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Bookseller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraries.library')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Libraire',
                'verbose_name_plural': 'Libraires',
                'ordering': ['-created_at'],
            },
        ),
    ]
