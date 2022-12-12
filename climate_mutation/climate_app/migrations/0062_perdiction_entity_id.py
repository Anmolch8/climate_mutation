# Generated by Django 4.1.1 on 2022-11-24 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("climate_app", "0061_perdiction"),
    ]

    operations = [
        migrations.AddField(
            model_name="perdiction",
            name="entity_id",
            field=models.ForeignKey(
                blank=True,
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="climate_app.entitie",
            ),
            preserve_default=False,
        ),
    ]
