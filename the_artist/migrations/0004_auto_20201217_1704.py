# Generated by Django 3.1 on 2020-12-17 15:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('the_artist', '0003_auto_20201217_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='titlu', max_length=100)),
                ('paragraf', models.TextField()),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.AlterField(
            model_name='audiomixes',
            name='image',
            field=models.ImageField(default='default-image.png', upload_to='media'),
        ),
        migrations.AlterField(
            model_name='facebooklive',
            name='image',
            field=models.ImageField(default='default-image.png', upload_to='media'),
        ),
        migrations.AlterField(
            model_name='imagesprime',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='prime',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 17, 15, 4, 13, 227445, tzinfo=utc)),
        ),
    ]
