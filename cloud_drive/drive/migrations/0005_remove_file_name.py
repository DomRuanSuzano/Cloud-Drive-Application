# Generated by Django 5.1.2 on 2024-11-06 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0004_file_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='name',
        ),
    ]