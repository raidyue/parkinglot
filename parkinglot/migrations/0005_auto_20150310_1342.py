# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkinglot', '0004_auto_20150309_0614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consuption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField(verbose_name=b'start parking time')),
                ('end_time', models.DateTimeField(verbose_name=b'end parking time')),
                ('order_time', models.DateTimeField(verbose_name=b'order time')),
                ('lot', models.ForeignKey(to='parkinglot.Lot')),
                ('parkinglot', models.ForeignKey(to='parkinglot.Parkinglot')),
                ('user', models.ForeignKey(to='parkinglot.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='comsuption',
            name='lot',
        ),
        migrations.RemoveField(
            model_name='comsuption',
            name='parkinglot',
        ),
        migrations.RemoveField(
            model_name='comsuption',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comsuption',
        ),
    ]
