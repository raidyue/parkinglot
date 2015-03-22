# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkinglot', '0008_auto_20150317_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manager_name', models.CharField(unique=True, max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('parkinglot', models.ForeignKey(to='parkinglot.Parkinglot')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='consumption',
            name='status',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
