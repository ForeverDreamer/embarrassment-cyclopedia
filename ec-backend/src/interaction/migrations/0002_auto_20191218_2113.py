# Generated by Django 2.2.1 on 2019-12-18 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0015_delete_comment'),
        ('interaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='likeinfo',
            options={'verbose_name': 'LikeInfo', 'verbose_name_plural': 'LikeInfos'},
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='interaction.Comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
