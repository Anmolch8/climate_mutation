# Generated by Django 4.1.1 on 2022-10-01 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("climate_app", "0023_user_register_address_user_register_city_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_register",
            name="dob",
            field=models.DateField(blank=True, null=True, verbose_name="dd/mm/yyyy"),
        ),
    ]
