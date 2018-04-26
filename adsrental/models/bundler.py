from __future__ import unicode_literals

import decimal

from django.db import models


class Bundler(models.Model):
    '''
    Stores a single bundler entry, used to get bundler info for lead by *utm_source*
    '''
    PAYMENT = round(150.00, 2)
    CHARGEBACK_PAYMENT = round(50.00, 2)

    name = models.CharField(max_length=255, unique=True, db_index=True)
    utm_source = models.CharField(max_length=50, db_index=True, null=True, blank=True)
    adsdb_id = models.IntegerField(null=True, blank=True, help_text='ID from adsdb database')
    email = models.CharField(max_length=255, null=True, blank=True)
    skype = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    bank_info = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, help_text='If inactive, landing/sugnup page will not be shown for this utm_source.')
    enable_chargeback = models.BooleanField(default=True, help_text='If inactive, no chargeback will be calculated for lead accounts.')
    facebook_payment = models.DecimalField(default=decimal.Decimal(125.00), max_digits=8, decimal_places=2, help_text='Payout for facebook accounts')
    google_payment = models.DecimalField(default=decimal.Decimal(125.00), max_digits=8, decimal_places=2, help_text='Payout for google accounts')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @classmethod
    def get_by_utm_source(cls, utm_source):
        return cls.objects.filter(utm_source=utm_source).first()

    @classmethod
    def get_by_adsdb_id(cls, adsdb_id):
        return cls.objects.filter(adsdb_id=adsdb_id).first()

    def __str__(self):
        return self.name
        # return '{} ({})'.format(self.name, self.utm_source)
