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

LiveData.objects.all().delete()
ZebpayHistory.objects.all().delete()

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
	zebpay = LiveData.objects.get(siteId = 1, currency = 'INR')
	if data['buy'] != zebpay.buy and data['sell'] != zebpay.sell:
		zebpay.buy = data['buy']
		zebpay.sell = data['sell']
		zebpay.save()
		zebpayHistory = ZebpayHistory();
		zebpayHistory.buy = 1
		zebpayHistory.sell = 2
		zebpayHistory.buyFees = 0
		zebpayHistory.sellFees = 0
		zebpayHistory.siteId = 4
		zebpayHistory.timestamp = datetime.datetime.now()
		zebpayHistory.save()
	response = requests.get("https://api.zebpay.com/api/v1/ticker?currencyCode=SGD")
	data = response.json()
	if data['buy'] != zebpay.buy and data['sell'] != zebpay.sell:
		zebpay.buy = data['buy']
		zebpay.sell = data['sell']
		zebpay.save()
		zebpayHistory = ZebpayHistory();
		zebpayHistory.buy = 1
		zebpayHistory.sell = 2
		zebpayHistory.buyFees = 0
		zebpayHistory.sellFees = 0
		zebpayHistory.siteId = 4
		zebpayHistory.timestamp = datetime.datetime.now()
		zebpayHistory.save()
	response = requests.get("https://api.zebpay.com/api/v1/ticker?currencyCode=USD")
	data = response.json()
	zebpay = LiveData.objects.get(siteId = 1, currency = 'USD')#.objects.get_or_create(id=1);
	if data['buy'] != zebpay.buy and data['sell'] != zebpay.sell:
		zebpay.buy = data['buy']
		zebpay.sell = data['sell']
		zebpay.save()
		zebpayHistory = ZebpayHistory();
		zebpayHistory.buy = 1
		zebpayHistory.sell = 2
		zebpayHistory.buyFees = 0
		zebpayHistory.sellFees = 0
		zebpayHistory.siteId = 4
		zebpayHistory.timestamp = datetime.datetime.now()
		zebpayHistory.save()
	response = requests.get("https://www.coinhako.com/api/v1/price/currency/BTCSGD")
	data = response.json()
	zebpay = LiveData.objects.get(siteId = 3, currency = 'SGD')#.objects.get_or_create(id=1);
	zebpay.buy = data['data']['buy_price']
	zebpay.sell = data['data']['sell_price']
	zebpay.save()
	response = requests.get("https://www.coinhako.com/api/v1/price/currency/BTCUSD")
	data = response.json()
	zebpay = LiveData.objects.get(siteId = 3, currency = 'USD')#.objects.get_or_create(id=1);
	zebpay.buy = data['data']['buy_price']
	zebpay.sell = data['data']['sell_price']
	zebpay.save()
	print("YAG")
	# else:
	# 	zebpay.buy = data['buy']
	# 	zebpay.sell = data['sell']
	# 	zebpay.save()

while 1:
   liveData()
   time.sleep(30)


	

