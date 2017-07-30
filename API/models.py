from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class LiveData(models.Model):
    buy = models.DecimalField(decimal_places=10, max_digits=20)
    sell = models.DecimalField(decimal_places=10, max_digits=20)
    buyFees = models.DecimalField(decimal_places=10, max_digits=20)
    sellFees = models.DecimalField(decimal_places=10, max_digits=20)
    siteId = models.IntegerField()
    currency = models.CharField(max_length=255)

class ZebpayHistory(models.Model):
    buy = models.DecimalField(decimal_places=10, max_digits=20)
    sell = models.DecimalField(decimal_places=10, max_digits=20)
    currency = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)

class CoinhakoHistory(models.Model):
    buy = models.DecimalField(decimal_places=10, max_digits=20)
    sell = models.DecimalField(decimal_places=10, max_digits=20)
    currency = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)

class CoinbaseHistory(models.Model):
    buy = models.DecimalField(decimal_places=10, max_digits=20)
    sell = models.DecimalField(decimal_places=10, max_digits=20)
    currency = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)