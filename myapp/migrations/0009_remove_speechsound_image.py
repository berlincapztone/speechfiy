# Generated by Django 5.1.1 on 2024-10-21 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0008_speechsound"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="speechsound",
            name="image",
        ),
    ]
