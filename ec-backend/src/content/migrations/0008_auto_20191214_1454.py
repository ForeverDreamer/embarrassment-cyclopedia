# Generated by Django 2.2.1 on 2019-12-14 06:54

import content.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20191214_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postvideo',
            name='video',
            field=models.FileField(upload_to=content.models.post_video_upload),
        ),
    ]
