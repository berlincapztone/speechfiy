# Generated by Django 5.1.1 on 2024-10-18 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_phonemeexample_phoneticsymbol_phoneme_examples"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="phoneticsymbol",
            name="phoneme_examples",
        ),
        migrations.DeleteModel(
            name="PhonemeExample",
        ),
    ]
