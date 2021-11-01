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
