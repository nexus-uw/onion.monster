# Generated by Django 5.1.4 on 2025-01-08 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Record",
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
                ("domain", models.CharField(max_length=200)),
                ("key", models.CharField(max_length=64)),
                ("lastUpdated", models.DateField()),
            ],
        ),
    ]