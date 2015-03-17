# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkinglot', '0002_auto_20150309_0556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comsuption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField(verbose_name=b'start parking time')),
                ('end_time', models.DateTimeField(verbose_name=b'end parking time')),
                ('order_time', models.DateTimeField(verbose_name=b'order time')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.CharField(max_length=10)),
                ('status', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parkinglot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=80)),
                ('charge', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='lot',
            name='pid',
            field=models.ForeignKey(to='parkinglot.Parkinglot'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comsuption',
            name='lid',
            field=models.ForeignKey(to='parkinglot.Lot'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comsuption',
            name='pid',
            field=models.ForeignKey(to='parkinglot.Parkinglot'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comsuption',
            name='uid',
            field=models.ForeignKey(to='parkinglot.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='over',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
