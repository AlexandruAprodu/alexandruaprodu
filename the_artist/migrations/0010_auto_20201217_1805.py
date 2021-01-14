# Generated by Django 3.1 on 2020-12-17 16:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('the_artist', '0009_auto_20201217_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audiomixes',
            old_name='embed',
            new_name='url',
        ),
        migrations.AlterField(
            model_name='prime',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 17, 16, 5, 48, 823517, tzinfo=utc)),
        ),
    ]
