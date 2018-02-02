# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-02 20:58
from __future__ import unicode_literals

from django.db import migrations, models


def populate_sf_leadid(apps, schema_editor):
    Lead = apps.get_model('adsrental', 'Lead')
    for lead in Lead.objects.all():
        lead.sf_leadid = lead.leadid
        lead.save()


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0048_auto_20180202_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='sf_leadid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.RunPython(populate_sf_leadid, reverse_code=migrations.RunPython.noop),
    ]
