# Generated by Django 2.2.1 on 2019-10-12 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20191012_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thirdpartyinfo',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='thirdpartyinfo',
            name='image_width',
        ),
    ]
