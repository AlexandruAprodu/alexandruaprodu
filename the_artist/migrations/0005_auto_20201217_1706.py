# Generated by Django 3.1 on 2020-12-17 15:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('the_artist', '0004_auto_20201217_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audiomixes',
            old_name='link',
            new_name='embed',
        ),
        migrations.RemoveField(
            model_name='audiomixes',
            name='image',
        ),
        migrations.RemoveField(
            model_name='audiomixes',
            name='paragraf',
        ),
        migrations.AlterField(
            model_name='prime',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 17, 15, 6, 22, 678641, tzinfo=utc)),
        ),
    ]