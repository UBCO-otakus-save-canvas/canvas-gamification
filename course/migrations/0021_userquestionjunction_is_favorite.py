# Generated by Django 3.0.14 on 2021-11-01 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0020_question_question_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='userquestionjunction',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
