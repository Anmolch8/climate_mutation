# Generated by Django 4.1.1 on 2022-09-27 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("climate_app", "0013_remove_user_register_user_name_user_register_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_register",
            name="email",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]