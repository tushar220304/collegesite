# Generated by Django 3.2.15 on 2022-10-06 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20221006_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='enrollmentno',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
