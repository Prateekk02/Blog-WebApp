# Generated by Django 5.0.6 on 2024-06-01 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blogcontent_thumbnail_alter_blogcontent_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcontent',
            name='thumbnail',
            field=models.ImageField(upload_to='blog_thumbnails/'),
        ),
    ]