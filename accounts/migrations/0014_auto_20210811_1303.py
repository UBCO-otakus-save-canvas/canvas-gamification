# Generated by Django 3.0.14 on 2021-08-11 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20210608_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='userconsent',
            name='access_course_grades',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userconsent',
            name='access_submitted_course_work',
            field=models.BooleanField(default=False),
        ),
    ]