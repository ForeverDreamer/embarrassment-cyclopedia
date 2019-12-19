# Generated by Django 2.2.1 on 2019-12-14 05:55

import content.models
import content.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20191214_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postvideo',
            name='video',
            field=models.FileField(upload_to=content.models.post_video_upload, validators=[content.validators.validate_file_type]),
        ),
    ]