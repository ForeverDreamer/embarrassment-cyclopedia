# Generated by Django 2.2.1 on 2019-12-13 05:37

import content.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20191213_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('body', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='desc',
        ),
        migrations.RemoveField(
            model_name='post',
            name='article_id',
        ),
        migrations.AddField(
            model_name='post',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('image ', '图文'), ('video', '视频')], max_length=10),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('title_pic', models.CharField(max_length=120)),
                ('desc', models.CharField(max_length=120)),
                ('active', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Category')),
            ],
        ),
        migrations.CreateModel(
            name='PostVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=content.models.post_video_upload)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.Article'),
        ),
    ]
