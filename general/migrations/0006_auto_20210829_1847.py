# Generated by Django 3.0.14 on 2021-08-30 01:47

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_auto_20201120_1808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='action',
            old_name='user',
            new_name='actor',
        ),
        migrations.AddField(
            model_name='action',
            name='data',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='action',
            name='object_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='action',
            name='object_type',
            field=models.CharField(choices=[('Question', 'Question'), ('User', 'User'), ('Submission', 'Submission'), ('Course', 'Course'), ('Event', 'Event'), ('Course Registration', 'Course Registration')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='action',
            name='verb',
            field=models.CharField(choices=[('Created', 'Created'), ('Completed', 'Completed'), ('Opened', 'Opened'), ('Deleted', 'Deleted'), ('Delivered', 'Delivered'), ('Read', 'Read'), ('Solved', 'Solved'), ('Submitted', 'Submitted'), ('Sent', 'Sent'), ('Started', 'Started'), ('Used', 'Used'), ('Registered', 'Registered'), ('Edited', 'Edited'), ('Unread', 'Unread'), ('Skipped', 'Skipped'), ('Logged In', 'Logged In'), ('Logged Out', 'Logged Out')], default='Completed', max_length=100),
            preserve_default=False,
        ),
    ]
