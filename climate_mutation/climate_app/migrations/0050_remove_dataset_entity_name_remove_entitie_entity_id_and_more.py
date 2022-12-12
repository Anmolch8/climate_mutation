# Generated by Django 4.1.1 on 2022-11-11 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("climate_app", "0049_alter_dataset_entity_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dataset",
            name="entity_name",
        ),
        migrations.RemoveField(
            model_name="entitie",
            name="entity_id",
        ),
        migrations.AddField(
            model_name="entitie",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=1,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
    ]
