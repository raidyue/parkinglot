# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkinglot', '0009_auto_20150321_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manager',
            old_name='manager_name',
            new_name='name',
        ),
    ]
