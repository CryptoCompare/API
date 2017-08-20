from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class BitcoinLiveData(models.Model):
    buy = models.DecimalField(decimal_places=10, max_digits=20)
    sell = models.DecimalField(decimal_places=10, max_digits=20)
    buyFees = models.DecimalField(decimal_places=10, max_digits=20)
    sellFees = models.DecimalField(decimal_places=10, max_digits=20)
    siteId = models.IntegerField()
    currency = models.CharField(max_length=255)
    lastHourMinBuy = models.DecimalField(decimal_places=10, max_digits=20, default = -1)
    lastDayMinBuy = models.DecimalField(decimal_places=10, max_digits=20, default = -1)
    lastWeekMinBuy = models.DecimalField(decimal_places=10, max_digits=20, default = -1)
    lastMonthMinBuy = models.DecimalField(decimal_places=10, max_digits=20, default = -1)
    lastHourMaxBuy = models.DecimalField(decimal_places=10, max_digits=20, default = -1)
    lastDayMaxBuy = models.DecimalField(decimal_places=10, max_digits=20, default = -1)
    lastWeekMaxBuy = models.DecimalField(decimal_places=10, max_digits=20, default = -1)
    lastMonthMaxBuy = models.DecimalField(decimal_places=10, max_digits=20, default = -1)
    lastHourMinSell = models.DecimalField(decimal_places=10, max_digits=20, default = -1)
    lastDayMinSell = models.DecimalField(decimal_places=10, max_digits=20, default = -1)
    lastWeekMinSell = models.DecimalField(decimal_places=10, max_digits=20, default = -1)
    lastMonthMinSell = models.DecimalField(decimal_places=10, max_digits=20, default = -1)
    lastHourMaxSell = models.DecimalField(decimal_places=10, max_digits=20, default = -1)
    lastDayMaxSell = models.DecimalField(decimal_places=10, max_digits=20, default = -1)
    lastWeekMaxSell = models.DecimalField(decimal_places=10, max_digits=20, default = -1)
    lastMonthMaxSell = models.DecimalField(decimal_places=10, max_digits=20, default = -1)

class BitcoinHistory(models.Model):
    siteId = models.IntegerField()
    buy = models.DecimalField(decimal_places=10, max_digits=20)
    sell = models.DecimalField(decimal_places=10, max_digits=20)
    currency = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)