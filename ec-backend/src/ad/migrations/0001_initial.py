# Generated by Django 2.2.1 on 2019-12-17 10:28

import ad.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('carousel ', '动态轮播图'), ('personal_center', '个人中心')], max_length=20)),
                ('url', models.CharField(max_length=50)),
                ('image_height', models.IntegerField(blank=True, null=True)),
                ('image_width', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, height_field='image_height', null=True, upload_to=ad.models.ad_image_upload, width_field='image_width')),
            ],
            options={
                'verbose_name': 'AdInfo',
                'verbose_name_plural': 'AdInfos',
            },
        ),
    ]
