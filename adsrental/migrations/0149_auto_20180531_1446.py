# Generated by Django 2.0.5 on 2018-05-31 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsrental', '0148_leadaccount_banned_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerioevent',
            name='name',
            field=models.CharField(choices=[('shipped', 'Shipped'), ('delivered', 'Delivered'), ('offline', 'Offline'), ('lead_approved', 'Approved'), ('banned', 'Banned'), ('available_banned', 'Banned from available status'), ('banned_has_accounts', 'Banned but has other active accounts'), ('security_checkpoint', 'Security checkpoint reported')], help_text='Event name. Used in customer.io filters.', max_length=255),
        ),
        migrations.AlterField(
            model_name='leadaccount',
            name='account_type',
            field=models.CharField(choices=[('Facebook', 'Facebook'), ('Google', 'Google'), ('Amazon', 'Amazon')], max_length=50),
        ),
    ]
