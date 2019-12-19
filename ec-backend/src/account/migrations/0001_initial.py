# Generated by Django 2.2.1 on 2019-12-16 03:00

import account.models
import account.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ThirdLoginInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('third_type', models.CharField(choices=[('wechat', '微信'), ('microblog', '微博'), ('qq', 'QQ'), ('others', '其他')], default='others', max_length=50)),
                ('openid', models.CharField(max_length=200, unique=True)),
                ('nickname', models.CharField(max_length=50)),
                ('logout', models.BooleanField(default=True)),
                ('image_height', models.IntegerField(blank=True, null=True)),
                ('image_width', models.IntegerField(blank=True, null=True)),
                ('third_user_pic', models.ImageField(blank=True, height_field='image_height', null=True, upload_to=account.models.third_user_pic_upload, width_field='image_width')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='third_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ThirdLoginInfo',
                'verbose_name_plural': 'ThirdLoginInfos',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_height', models.IntegerField(blank=True, null=True)),
                ('image_width', models.IntegerField(blank=True, null=True)),
                ('user_pic', models.ImageField(blank=True, height_field='image_height', null=True, upload_to=account.models.user_pic_upload, width_field='image_width')),
                ('mobile_phone', models.CharField(blank=True, max_length=50, null=True, validators=[account.validators.validate_mobile_phone])),
                ('cteate_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('gender', models.CharField(choices=[('male ', '男'), ('female', '女'), ('secret', '保密')], default='secret', max_length=50)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('emotion', models.CharField(choices=[('single ', '单身'), ('in_love', '热恋'), ('married', '已婚'), ('secret', '保密')], default='secret', max_length=50)),
                ('career', models.CharField(choices=[('teacher ', '教师'), ('it', 'IT'), ('public_servant', '公务员'), ('secret', '保密')], default='secret', max_length=50)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('hometown', models.CharField(blank=True, max_length=50, null=True)),
                ('logout', models.BooleanField(default=False)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]