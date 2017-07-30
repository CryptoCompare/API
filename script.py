import os
import requests
import schedule
import time
import datetime
from coinbase.wallet.client import Client
import math

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "APIapp.settings")
import django
django.setup()

# your imports, e.g. Django models
from API.models import LiveData
from API.models import ZebpayHistory
from API.models import CoinhakoHistory
from API.models import CoinbaseHistory

LiveData.objects.all().delete()
# ZebpayHistory.objects.all().delete()

# zebpay = ZebpayHistory.objects.all()
# print (zebpay)

#1=zebpay 2=coinbase 3=coinhako 4=fybsg
currency  = ['USD', 'INR', 'SGD']
for i in range(1,4):
	for j in range(len(currency)):
		data = LiveData()
		data.buy = 0
		data.sell = 0
		data.buyFees = 0
		data.sellFees = 0
		data.siteId = i
		data.currency = currency[j]
		data.save()
#print(LiveData.objects.all().count())
def liveData():
	response = requests.get("https://api.zebpay.com/api/v1/ticker?currencyCode=INR")
	data = response.json()
	cur = LiveData.objects.get(siteId = 1, currency = 'INR')
	# print (data['buy'],data['sell'])
	if not math.isclose(data['buy'],cur.buy,rel_tol=1e-11) or not math.isclose(data['sell'],cur.sell,rel_tol=1e-11):
		cur.buy = data['buy']
		cur.sell = data['sell']
		cur.save()
		history = ZebpayHistory();
		history.buy = data['buy']
		history.sell = data['sell']
		history.currency = 'INR'
		history.timestamp = datetime.datetime.now()
		history.save()
	response = requests.get("https://api.zebpay.com/api/v1/ticker?currencyCode=SGD")
	data = response.json()
	cur = LiveData.objects.get(siteId = 1, currency = 'SGD')
	# print (data['buy'],data['sell'])
	if not math.isclose(data['buy'],cur.buy,rel_tol=1e-11) or not math.isclose(data['sell'],cur.sell,rel_tol=1e-11):
		cur.buy = data['buy']
		cur.sell = data['sell']
		cur.save()
		history = ZebpayHistory();
		history.buy = data['buy']
		history.sell = data['sell']
		history.currency = 'SGD'
		history.timestamp = datetime.datetime.now()
		history.save()
	response = requests.get("https://api.zebpay.com/api/v1/ticker?currencyCode=USD")
	data = response.json()
	cur = LiveData.objects.get(siteId = 1, currency = 'USD')
	# print (data['buy'],data['sell'])
	if not math.isclose(data['buy'],cur.buy,rel_tol=1e-11) or not math.isclose(data['sell'],cur.sell,rel_tol=1e-11):
		cur.buy = data['buy']
		cur.sell = data['sell']
		cur.save()
		history = ZebpayHistory();
		history.buy = data['buy']
		history.sell = data['sell']
		history.currency = 'USD'
		history.timestamp = datetime.datetime.now()
		history.save()
	response = requests.get("https://www.coinhako.com/api/v1/price/currency/BTCSGD")
	data = response.json()
	cur = LiveData.objects.get(siteId = 3, currency = 'SGD')
	# print (data['buy'],data['sell'])
	if not math.isclose(float(data['data']['buy_price']),cur.buy,rel_tol=1e-11) or not math.isclose(float(data['data']['sell_price']),cur.sell,rel_tol=1e-11):
		cur.buy = float(data['data']['buy_price'])
		cur.sell = float(data['data']['sell_price'])
		cur.save()
		history = CoinhakoHistory();
		history.buy = float(data['data']['buy_price'])
		history.sell = float(data['data']['sell_price'])
		history.currency = 'SGD'
		history.timestamp = datetime.datetime.now()
		history.save()
	response = requests.get("https://www.coinhako.com/api/v1/price/currency/BTCUSD")
	data = response.json()
	cur = LiveData.objects.get(siteId = 3, currency = 'USD')
	# print (data['buy'],data['sell'])
	if not math.isclose(float(data['data']['buy_price']),cur.buy,rel_tol=1e-11) or not math.isclose(float(data['data']['sell_price']),cur.sell,rel_tol=1e-11):
		cur.buy = data['data']['buy_price']
		cur.sell = data['data']['sell_price']
		cur.save()
		history = CoinhakoHistory();
		history.buy = data['data']['buy_price']
		history.sell = data['data']['sell_price']
		history.currency = 'USD'
		history.timestamp = datetime.datetime.now()
		history.save()
	response = requests.get("https://www.coinhako.com/api/v1/price/currency/BTCSGD")
	data = response.json()
	cur = LiveData.objects.get(siteId = 3, currency = 'SGD')
	# print (data['buy'],data['sell'])
	if not math.isclose(float(data['data']['buy_price']),cur.buy,rel_tol=1e-11) or not math.isclose(float(data['data']['sell_price']),cur.sell,rel_tol=1e-11):
		cur.buy = data['data']['buy_price']
		cur.sell = data['data']['sell_price']
		cur.save()
		history = CoinhakoHistory();
		history.buy = data['data']['buy_price']
		history.sell = data['data']['sell_price']
		history.currency = 'SGD'
		history.timestamp = datetime.datetime.now()
		history.save()	
	response = requests.get("https://api.coinbase.com/v2/prices/buy?currency=USD")
	data = response.json()
	response = requests.get("https://api.coinbase.com/v2/prices/sell?currency=USD")
	data2 = response.json()
	cur = LiveData.objects.get(siteId = 2, currency = 'USD')
	if not math.isclose(float(data['data']['amount']),cur.buy,rel_tol=1e-11) or not math.isclose(float(data2['data']['amount']),cur.sell,rel_tol=1e-11):
		cur.buy = data['data']['amount']
		cur.sell = data2['data']['amount']
		cur.save()
		history = CoinbaseHistory();
		history.buy = data['data']['amount']
		history.sell = data2['data']['amount']
		history.currency = 'USD'
		history.timestamp = datetime.datetime.now()
		history.save()
	response = requests.get("https://api.coinbase.com/v2/prices/buy?currency=SGD")
	data = response.json()
	response = requests.get("https://api.coinbase.com/v2/prices/sell?currency=SGD")
	data2 = response.json()
	cur = LiveData.objects.get(siteId = 2, currency = 'SGD')
	if not math.isclose(float(data['data']['amount']),cur.buy,rel_tol=1e-11) or not math.isclose(float(data2['data']['amount']),cur.sell,rel_tol=1e-11):
		cur.buy = data['data']['amount']
		cur.sell = data2['data']['amount']
		cur.save()
		history = CoinbaseHistory();
		history.buy = data['data']['amount']
		history.sell = data2['data']['amount']
		history.currency = 'SGD'
		history.timestamp = datetime.datetime.now()
		history.save()
while 1:
   liveData()
   time.sleep(30)


	

