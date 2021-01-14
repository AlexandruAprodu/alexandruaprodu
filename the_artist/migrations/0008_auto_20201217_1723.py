# Generated by Django 3.1 on 2020-12-17 15:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('the_artist', '0007_auto_20201217_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiomixes',
            name='embed',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='prime',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 17, 15, 23, 51, 488353, tzinfo=utc)),
        ),
    ]
