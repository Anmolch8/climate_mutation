# Generated by Django 4.1.1 on 2022-09-21 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("climate_app", "0008_expert_conatct"),
    ]

    operations = [
        migrations.AddField(
            model_name="expert",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="expert_pics"),
        ),
    ]
