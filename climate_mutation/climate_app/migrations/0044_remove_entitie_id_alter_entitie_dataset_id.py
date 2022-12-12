# Generated by Django 4.1.1 on 2022-11-11 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("climate_app", "0043_entitie_dataset_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="entitie",
            name="id",
        ),
        migrations.AlterField(
            model_name="entitie",
            name="dataset_id",
            field=models.PositiveIntegerField(
                blank=True, primary_key=True, serialize=False
            ),
        ),
    ]
