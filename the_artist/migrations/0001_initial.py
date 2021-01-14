# Generated by Django 3.1 on 2020-12-16 13:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioMixes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('paragraf', models.TextField()),
                ('image', models.ImageField(default='default-image.png', upload_to='post_pics')),
                ('link', models.CharField(max_length=130)),
            ],
        ),
        migrations.CreateModel(
            name='FacebookLive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('paragraf', models.TextField()),
                ('image', models.ImageField(default='default-image.png', upload_to='post_pics')),
                ('link', models.CharField(max_length=130)),
            ],
        ),
        migrations.CreateModel(
            name='Prime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('paragraf', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 12, 16, 13, 18, 44, 226967, tzinfo=utc))),
                ('image', models.ImageField(default='default-image.png', upload_to='post_pics')),
                ('link', models.CharField(max_length=130)),
            ],
        ),
    ]