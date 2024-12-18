# Generated by Django 5.1.1 on 2024-10-21 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0007_phoneticrepresentation"),
    ]

    operations = [
        migrations.CreateModel(
            name="SpeechSound",
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
                ("phoneme", models.CharField(max_length=10)),
                ("word", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="phonemes/images/")),
                (
                    "sound_phoneme",
                    models.FileField(blank=True, upload_to="phonemes/sounds/"),
                ),
                (
                    "sound_word",
                    models.FileField(blank=True, upload_to="phonemes/sounds/"),
                ),
            ],
        ),
    ]
