# Generated by Django 2.2.1 on 2019-10-13 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='slug',
        ),
    ]
