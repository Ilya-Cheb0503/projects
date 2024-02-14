# Generated by Django 5.0 on 2023-12-16 07:34

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ColivingImage",
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
                ("image", models.ImageField(upload_to="images/")),
                (
                    "file_id",
                    models.UUIDField(
                        db_index=True,
                        default=uuid.uuid4,
                        editable=False,
                        unique=True,
                    ),
                ),
                (
                    "coliving",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="profiles.coliving",
                    ),
                ),
            ],
            options={
                "verbose_name": "Фото коливинга",
                "verbose_name_plural": "Фото коливингов",
                "abstract": False,
                "default_related_name": "images",
            },
        ),
        migrations.CreateModel(
            name="ProfileImage",
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
                ("image", models.ImageField(upload_to="images/")),
                (
                    "file_id",
                    models.UUIDField(
                        db_index=True,
                        default=uuid.uuid4,
                        editable=False,
                        unique=True,
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="profiles.profile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Фото пользователя",
                "verbose_name_plural": "Фото пользователей",
                "abstract": False,
                "default_related_name": "images",
            },
        ),
    ]