# Generated by Django 2.2.1 on 2019-10-12 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_thirdpartyinfo_logout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thirdpartyinfo',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='third', to=settings.AUTH_USER_MODEL),
        ),
    ]
