# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-25 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0042_remove_ec2instance_raspberry_pi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raspberrypi',
            name='version',
            field=models.CharField(default=b'1.0.1', max_length=20),
        ),
    ]
