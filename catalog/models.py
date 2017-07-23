from __future__ import unicode_literals
from django.db import models


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
    buyFees = models.DecimalField(decimal_places=10, max_digits=20)
    sellFees = models.DecimalField(decimal_places=10, max_digits=20)
    siteId = models.IntegerField()
    timestamp = models.DateTimeField()