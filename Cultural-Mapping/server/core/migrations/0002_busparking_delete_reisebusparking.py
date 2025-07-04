# Generated by Django 5.2.3 on 2025-06-25 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BusParking",
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
                ("number", models.IntegerField()),
                ("location", models.CharField(max_length=255)),
                ("capacity", models.CharField(max_length=100)),
                ("cost", models.CharField(max_length=100)),
                ("remarks", models.TextField(blank=True, null=True)),
                ("x", models.FloatField()),
                ("y", models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name="ReisebusParking",
        ),
    ]
