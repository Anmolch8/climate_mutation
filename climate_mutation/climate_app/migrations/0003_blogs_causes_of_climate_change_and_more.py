# Generated by Django 4.1.1 on 2022-09-19 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("climate_app", "0002_disaster"),
    ]

    operations = [
        migrations.CreateModel(
            name="blogs",
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
                ("title", models.CharField(max_length=3000)),
                ("image", models.ImageField(blank=True, upload_to="blogs_pics")),
                ("description", models.TextField()),
                ("added_on", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="causes_of_climate_change",
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
                ("title", models.CharField(max_length=3000)),
                (
                    "image",
                    models.ImageField(blank=True, upload_to="climate_change_pics"),
                ),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="effects_of_climate_change",
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
                ("title", models.CharField(max_length=3000)),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to="climate_change_effects_pics"
                    ),
                ),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="experts",
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
                ("name", models.CharField(max_length=500)),
                ("expertise", models.CharField(max_length=500)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="faqs",
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
                ("question", models.TextField()),
                ("answer", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="images_of_changes",
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
                ("from_date", models.DateField()),
                ("to_date", models.DateField()),
                (
                    "before_image",
                    models.ImageField(blank=True, upload_to="change_pics"),
                ),
                ("after_image", models.ImageField(blank=True, upload_to="change_pics")),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="ngos",
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
                ("name", models.CharField(max_length=500)),
                ("cause", models.CharField(max_length=500)),
                ("website", models.URLField()),
                ("address", models.TextField()),
                ("contact_number", models.CharField(max_length=12)),
                ("logo", models.ImageField(blank=True, upload_to="ngos_pics")),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="ongoing_projects",
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
                ("name", models.CharField(max_length=500)),
                ("sponsored_by", models.CharField(max_length=500)),
                ("image", models.ImageField(blank=True, upload_to="projects_pics")),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="prevention_steps_for_climate_change",
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
                ("title", models.CharField(max_length=3000)),
                ("image", models.ImageField(blank=True, upload_to="prevention_pics")),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="videos",
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
                ("title", models.CharField(max_length=3000)),
                ("link", models.URLField()),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="volunteers",
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
                ("name", models.CharField(max_length=500)),
                ("image", models.ImageField(blank=True, upload_to="volunteer_pics")),
                ("about", models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name="disaster",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="disaster_pics"),
        ),
    ]
