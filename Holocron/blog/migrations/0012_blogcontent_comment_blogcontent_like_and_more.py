# Generated by Django 5.0.6 on 2024-06-02 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_blogcontent_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcontent',
            name='comment',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='blogcontent',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blogcontent',
            name='report',
            field=models.IntegerField(default=0),
        ),
    ]