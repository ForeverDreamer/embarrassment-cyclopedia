# Generated by Django 2.2.1 on 2019-12-17 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='nickname',
            field=models.CharField(default='用户_8888888888', max_length=50, unique=True),
            preserve_default=False,
        ),
    ]