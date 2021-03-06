# Generated by Django 2.0.7 on 2018-07-16 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0175_lead_shipstation_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='shipstation_order_status',
            field=models.CharField(blank=True, choices=[('shipped', 'Shipped'), ('awaiting_shipment', 'Awaiting'), ('on_hold', 'On Hold'), ('cancelled', 'Cancelled')], help_text='Populated by cron script.', max_length=100, null=True),
        ),
    ]
