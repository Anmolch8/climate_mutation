# Generated by Django 4.1.1 on 2022-09-27 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("climate_app", "0016_remove_user_register_emai_user_register_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_register",
            name="email",
            field=models.CharField(max_length=100),
        ),
    ]
