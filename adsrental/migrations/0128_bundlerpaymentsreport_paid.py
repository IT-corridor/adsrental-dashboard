# Generated by Django 2.0.3 on 2018-04-23 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0127_auto_20180423_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundlerpaymentsreport',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]