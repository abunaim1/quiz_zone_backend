# Generated by Django 5.0.1 on 2024-02-26 08:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_remove_question_question_paper_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_paper',
        ),
        migrations.AddField(
            model_name='question',
            name='question_paper',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='question.questionpaper'),
        ),
    ]
