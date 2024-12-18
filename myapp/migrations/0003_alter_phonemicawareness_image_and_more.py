# Generated by Django 5.1.1 on 2024-10-18 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_phonemicawareness"),
    ]

    operations = [
        migrations.AlterField(
            model_name="phonemicawareness",
            name="image",
            field=models.ImageField(upload_to="phonemes/images/"),
        ),
        migrations.AlterField(
            model_name="phonemicawareness",
            name="phoneme",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="phonemicawareness",
            name="sound",
            field=models.FileField(blank=True, upload_to="phonemes/sounds/"),
        ),
    ]
