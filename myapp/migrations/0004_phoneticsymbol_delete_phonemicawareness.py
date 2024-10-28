# Generated by Django 5.1.1 on 2024-10-18 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_alter_phonemicawareness_image_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PhoneticSymbol",
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
        migrations.DeleteModel(
            name="PhonemicAwareness",
        ),
    ]
