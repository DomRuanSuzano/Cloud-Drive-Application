# Generated by Django 5.1.2 on 2024-10-18 14:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("drive", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="file",
            name="name",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
