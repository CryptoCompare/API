import os
import requests
import schedule
import time
import datetime
from coinbase.wallet.client import Client
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drftutorial.settings")
import django
django.setup()

# your imports, e.g. Django models
from catalog.models import LiveData
from catalog.models import ZebpayHistory

response = requests.get("https://www.coinhako.com/api/v1/price/currency/BTCSGD")
data = response.json()
print (data['data']['buy_price'])