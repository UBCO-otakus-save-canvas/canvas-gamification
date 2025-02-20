# Generated by Django 3.0.14 on 2022-01-23 19:55

import course.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0024_auto_20211203_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmissionAnalytics',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('submission_type', models.CharField(default='n/a', max_length=255)),
                ('user_id', models.IntegerField(default=0)),
                ('first_name', models.CharField(default='n/a', max_length=255)),
                ('last_name', models.CharField(default='n/a', max_length=255)),
                ('ans_file', course.fields.JSONField(default=dict)),
                ('ans', models.CharField(default='n/a', max_length=255)),
                ('lines', models.IntegerField(default=0)),
                ('blank_lines', models.IntegerField(default=0)),
                ('comment_lines', models.IntegerField(default=0)),
                ('import_lines', models.IntegerField(default=0)),
                ('cc', models.IntegerField(default=0)),
                ('method', models.IntegerField(default=0)),
                ('operator', models.IntegerField(default=0)),
                ('operand', models.IntegerField(default=0)),
                ('unique_operator', models.IntegerField(default=0)),
                ('unique_operand', models.IntegerField(default=0)),
                ('vocab', models.IntegerField(default=0)),
                ('size', models.IntegerField(default=0)),
                ('vol', models.DecimalField(decimal_places=4, default=0, max_digits=8)),
                ('difficulty', models.DecimalField(decimal_places=4, default=0, max_digits=8)),
                ('effort', models.DecimalField(decimal_places=4, default=0, max_digits=8)),
                ('error', models.DecimalField(decimal_places=4, default=0, max_digits=8)),
                ('test_time', models.DecimalField(decimal_places=4, default=0, max_digits=8)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Question')),
                ('submission', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course.Submission')),
                ('uqj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.UserQuestionJunction')),
            ],
        ),
    ]
