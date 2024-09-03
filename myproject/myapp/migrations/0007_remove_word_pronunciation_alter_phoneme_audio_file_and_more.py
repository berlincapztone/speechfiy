# Generated by Django 5.0.6 on 2024-06-05 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_sightword1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='pronunciation',
        ),
        migrations.AlterField(
            model_name='phoneme',
            name='audio_file',
            field=models.FileField(upload_to='phoneme_audios'),
        ),
        migrations.AlterField(
            model_name='word',
            name='word',
            field=models.CharField(max_length=50),
        ),
    ]
