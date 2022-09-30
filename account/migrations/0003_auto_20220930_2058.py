# Generated by Django 3.2.15 on 2022-09-30 15:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='erollmentno',
        ),
        migrations.AddField(
            model_name='student',
            name='enrollmentno',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
