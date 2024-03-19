# Generated by Django 5.0.3 on 2024-03-15 11:24

import apps.music.utils
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Artist",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default="1f3149a0f60943a09f79469da5675094",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        default="avatar.jpeg", upload_to="artist/%Y/%m/%d"
                    ),
                ),
                ("fullname", models.CharField(max_length=128)),
                ("followers", models.IntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Genre",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=128)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Song",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128)),
                (
                    "cover",
                    models.ImageField(upload_to=apps.music.utils.song_cover_path),
                ),
                ("file", models.FileField(upload_to=apps.music.utils.song_file_path)),
                (
                    "genres",
                    models.ManyToManyField(related_name="songs", to="music.genre"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Album",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128)),
                (
                    "cover",
                    models.ImageField(upload_to=apps.music.utils.album_cover_path),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="music.artist"
                    ),
                ),
                ("songs", models.ManyToManyField(to="music.song")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
