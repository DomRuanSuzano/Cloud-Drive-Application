# Generated by Django 5.1.2 on 2024-10-18 14:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("drive", "0003_remove_file_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="file",
            name="name",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]