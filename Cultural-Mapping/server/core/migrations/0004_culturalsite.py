# Generated by Django 5.2.3 on 2025-06-26 17:04

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_motorhomeparking"),
    ]

    operations = [
        migrations.CreateModel(
            name="CulturalSite",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("tourism", models.CharField(blank=True, max_length=100, null=True)),
                ("website", models.URLField(blank=True, null=True)),
                ("operator", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "wheelchair_access",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("osm_id", models.CharField(max_length=100, unique=True)),
                (
                    "location",
                    django.contrib.gis.db.models.fields.PointField(
                        geography=True, srid=4326
                    ),
                ),
            ],
        ),
    ]
