# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-31 23:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0045_ec2instance_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='old_status',
            field=models.CharField(blank=True, choices=[('Available', 'Available'), ('Banned', 'Banned'), ('Qualified', 'Qualified'), ('In-Progress', 'In-Progress')], default=None, max_length=40, null=True),
        ),
    ]
