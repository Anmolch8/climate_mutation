# Generated by Django 4.1.1 on 2022-09-30 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("climate_app", "0021_reviews_user_name"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="reviews",
            new_name="review",
        ),
    ]