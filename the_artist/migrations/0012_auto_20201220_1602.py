# Generated by Django 3.1 on 2020-12-20 14:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('the_artist', '0011_auto_20201220_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facebooklive',
            name='paragraf',
        ),
        migrations.AlterField(
            model_name='prime',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 20, 14, 2, 17, 602237, tzinfo=utc)),
        ),
    ]