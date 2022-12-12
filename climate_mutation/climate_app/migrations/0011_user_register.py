# Generated by Django 4.1.1 on 2022-09-27 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("climate_app", "0010_alter_expert_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="user_register",
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
                ("fname", models.CharField(max_length=300)),
                ("lname", models.CharField(max_length=300)),
                ("user_name", models.CharField(max_length=500)),
                ("password", models.CharField(max_length=16)),
                ("confirm_password", models.CharField(max_length=16)),
            ],
        ),
    ]