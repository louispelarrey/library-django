# Generated by Django 3.2.16 on 2022-12-24 00:40

from django.db import migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='geom',
            field=djgeojson.fields.PointField(blank=True, null=True),
        ),
    ]
