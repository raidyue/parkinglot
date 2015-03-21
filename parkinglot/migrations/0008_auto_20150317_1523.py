# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkinglot', '0007_auto_20150312_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumption',
            name='end_time',
            field=models.DateTimeField(null=True, verbose_name=b'end parking time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='consumption',
            name='order_time',
            field=models.DateTimeField(null=True, verbose_name=b'order time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='consumption',
            name='start_time',
            field=models.DateTimeField(null=True, verbose_name=b'start parking time'),
            preserve_default=True,
        ),
    ]
