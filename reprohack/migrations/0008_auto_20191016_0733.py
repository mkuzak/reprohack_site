# Generated by Django 2.2.6 on 2019-10-16 07:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reprohack', '0007_auto_20191016_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time_end',
            field=models.TimeField(default=datetime.time(7, 33, 37, 485584)),
        ),
        migrations.AlterField(
            model_name='event',
            name='time_start',
            field=models.TimeField(default=datetime.time(7, 33, 37, 485551)),
        ),
    ]