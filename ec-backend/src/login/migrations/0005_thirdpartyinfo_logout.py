# Generated by Django 2.2.1 on 2019-10-12 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_profile_logout'),
    ]

    operations = [
        migrations.AddField(
            model_name='thirdpartyinfo',
            name='logout',
            field=models.BooleanField(default=True),
        ),
    ]
