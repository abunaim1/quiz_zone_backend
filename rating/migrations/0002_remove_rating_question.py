# Generated by Django 5.0.1 on 2024-02-28 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='question',
        ),
    ]