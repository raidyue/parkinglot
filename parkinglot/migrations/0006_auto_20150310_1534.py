# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkinglot', '0005_auto_20150310_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkinglot',
            name='name',
            field=models.CharField(unique=True, max_length=20),
            preserve_default=True,
        ),
    ]
