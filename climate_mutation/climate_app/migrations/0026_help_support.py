# Generated by Django 4.1.1 on 2022-10-06 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("climate_app", "0025_alter_user_register_dob"),
    ]

    operations = [
        migrations.CreateModel(
            name="help_support",
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
                ("user_name", models.CharField(max_length=500)),
                ("help_heading", models.CharField(max_length=5000)),
                ("help_description", models.TextField()),
            ],
        ),
    ]
