# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 13:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonito', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperatura',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
