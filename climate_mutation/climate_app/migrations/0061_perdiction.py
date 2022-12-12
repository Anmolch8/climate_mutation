# Generated by Django 4.1.1 on 2022-11-24 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("climate_app", "0060_delete_perdiction"),
    ]

    operations = [
        migrations.CreateModel(
            name="perdiction",
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
                ("perdiction_name", models.CharField(max_length=3000)),
                ("link", models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]
