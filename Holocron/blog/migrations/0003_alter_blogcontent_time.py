# Generated by Django 5.0.6 on 2024-05-31 16:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogcontent_content_alter_blogcontent_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcontent',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 31, 16, 58, 4, 624243, tzinfo=datetime.timezone.utc)),
        ),
    ]
