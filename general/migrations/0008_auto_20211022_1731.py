# Generated by Django 3.0.14 on 2021-10-23 00:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0020_question_question_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('general', '0007_auto_20210829_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='verb',
            field=models.CharField(choices=[('Created', 'Created'), ('Completed', 'Completed'), ('Opened', 'Opened'), ('Deleted', 'Deleted'), ('Delivered', 'Delivered'), ('Read', 'Read'), ('Solved', 'Solved'), ('Submitted', 'Submitted'), ('Sent', 'Sent'), ('Started', 'Started'), ('Used', 'Used'), ('Registered', 'Registered'), ('Edited', 'Edited'), ('Unread', 'Unread'), ('Skipped', 'Skipped'), ('Logged In', 'Logged In'), ('Logged Out', 'Logged Out'), ('Evaluated', 'Evaluated'), ('Updated', 'Updated')], max_length=100),
        ),
        migrations.CreateModel(
            name='QuestionReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('report', models.CharField(choices=[('TYPO_TEXT', 'There is a typo in the question instructions'), ('TYPO_ANSWER', 'There is a typo in one of the multiple-choice answers'), ('RIGHT_SOLUTION_MARKED_WRONG', 'My solution is definitely correct but it did not get full marks'), ('WRONG_SOLUTION_MARKED_RIGHT', 'My solution is incorrect but it received full marks'), ('OTHER', 'Other')], max_length=1000)),
                ('report_details', models.TextField(db_index=True, default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'question')},
            },
        ),
    ]
