# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-21 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0076_lead_ban_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='ban_reason',
            field=models.CharField(blank=True, choices=[('Google - Policy', 'Google - Policy'), ('Google - Billing', 'Google - Billing'), ('Google - Unresponsive User', 'Google - Unresponsive User'), ('Facebook - Policy', 'Facebook - Policy'), ('Facebook - Suspicious', 'Facebook - Suspicious'), ('Facebook - Lockout', 'Facebook - Lockout'), ('Facebook - Unresponsive User', 'Facebook - Unresponsive User')], max_length=40, null=True),
        ),
    ]