# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkinglot', '0003_auto_20150309_0611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comsuption',
            old_name='lid',
            new_name='lot',
        ),
        migrations.RenameField(
            model_name='comsuption',
            old_name='pid',
            new_name='parkinglot',
        ),
        migrations.RenameField(
            model_name='comsuption',
            old_name='uid',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='lot',
            old_name='pid',
            new_name='parkinglot',
        ),
    ]
