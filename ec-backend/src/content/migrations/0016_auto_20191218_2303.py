# Generated by Django 2.2.1 on 2019-12-18 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0015_delete_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='owner',
        ),
    ]
