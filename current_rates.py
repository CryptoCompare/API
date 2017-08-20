import requests as r
import json
import os
import schedule
import time
import datetime
from coinbase.wallet.client import Client
import math
import json
import datetime
from datetime import timedelta
from pprint import pprint
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "APIapp.settings")
import django
django.setup()
"""
API will contain 1, 2 or 3 fields in the JSON file

One: all the values exist in one JSON, volume will be null, if not provided by the API
Two: buy, sell, volume is not provided by the API
Three: if at least two of the three things(buy, sell, volume) differ


Validate in current_rates.py if volume is provided or not
"""

"""
Add in process exchanges here

More: [
	{
	  "name": "quoine",
	  "url": "https://developers.quoine.com/#introduction"
	},
	{
	  "name": "bittrex",
	  "url": "https://bittrex.com/Home/Api"
	}
]
"""
from API.models import BitcoinLiveData
from API.models import BitcoinHistory

BitcoinLiveData.objects.all().delete()

data = {
	"success": False,
	"buy": -1,
	"sell": -1,
	"volume": -1
}

def getRate(apiInfo):
	data['success'] = False
	data['buy'] = -1
	data['sell'] = -1
	data['volume'] = -1
	if(len(apiInfo)>0):
		if 'all' in apiInfo:
			api = apiInfo['all']
			if 'volumeKey' in api:
				sendRequest(api['endpoint'], api['buyKey'], api['sellKey'], api['volumeKey'])
			else:
				sendRequest(api['endpoint'], api['buyKey'], api['sellKey'], -1)
		else :
			apiBuy = apiInfo['buy']
			sendRequest(apiBuy['endpoint'], apiBuy['buyKey'], -1, -1)

			apiSell = apiInfo['sell']
			sendRequest(apiSell['endpoint'], -1, apiSell['sellKey'], -1)

			if 'volume' in apiInfo:
				apiVolume = apiInfo['volume']
				sendRequest(apiVolume['endpoint'], -1, -1, apiVolume['volumeKey'])

def sendRequest(url, buyKey, sellKey, volumeKey):
	response = r.get(url)
	responseJson = response.json()

	if response.status_code == 200:
		data['success'] = True

	# Loop because json data can be nested
	# Reassign val because val is being updated everytime in loop


	if buyKey != -1:
		buyKey = buyKey.split('.')
		val = responseJson
		for key in buyKey:
			val = val[key]
		data['buy'] = val

	if sellKey != -1:
		sellKey = sellKey.split('.')
		val = responseJson
		for key in sellKey:
			val = val[key]
		data['sell'] = val

	if volumeKey != -1:
		volumeKey = volumeKey.split('.')
		val = responseJson
		for key in volumeKey:
			val = val[key]
		data['volume'] = val

def getMin(time, currency, id):
	time_threshold = datetime.datetime.now() - timedelta(seconds = int(time))
	lastx = BitcoinHistory.objects.filter(currency = currency, siteId = id, timestamp__range=(time_threshold,datetime.datetime.now()))
	minBuy = float(9999999999999999999)
	minSell = float(9999999999999999999)
	maxBuy = float(0)
	maxSell = float(0)
	for val in lastx:
		minBuy = float(min(val.buy, minBuy))
		maxBuy = float(max(val.buy, maxBuy))
		minSell = float(min(val.sell, minSell))
		maxSell = float(max(val.sell, maxSell))

	return (minBuy, minSell, maxBuy, maxSell)

filename = "exchanges.json"

try:
	f = open(filename, 'r')
	json_data = json.loads(f.read())
	for key, value in json_data.items():
		for site in value:
			data1 = BitcoinLiveData()
			data1.buy = 0
			data1.sell = 0
			data1.buyFees = 0
			data1.sellFees = 0
			data1.siteId = site['id']
			data1.currency = key
			data1.lastHourMinBuy = -1;
			data1.lastDayMinBuy = -1;
			data1.lastWeekMinBuy = -1;
			data1.lastMonthMinBuy = -1;
			data1.lastHourMaxBuy = -1;
			data1.lastDayMaxBuy = -1;
			data1.lastWeekMaxBuy = -1;
			data1.lastMonthMaxBuy = -1;
			data1.lastHourMinSell = -1;
			data1.lastDayMinSell = -1;
			data1.lastWeekMinSell = -1;
			data1.lastMonthMinSell = -1;
			data1.lastHourMaxSell = -1;
			data1.lastDayMaxSell = -1;
			data1.lastWeekMaxSell = -1;
			data1.lastMonthMaxSell = -1;
			data1.save()
except IOError:
	print ('problem reading: ' + filename)

while 1:
	for key, value in json_data.items():
			for site in value:
				getRate(site['api'])
				cur = BitcoinLiveData.objects.get(siteId = site['id'], currency = key)
				cur.lastHourMinBuy, cur.lastHourMinSell, cur.lastHourMaxBuy, cur.lastHourMaxSell = getMin(3600, key, site['id'])
				cur.lastDayMinBuy, cur.lastDayMinSell, cur.lastDayMaxBuy, cur.lastDayMaxSell = getMin(86400, key, site['id'])
				cur.lastWeekMinBuy, cur.lastWeekMinSell, cur.lastWeekMaxBuy, cur.lastWeekMaxSell = getMin(604800, key, site['id'])
				cur.lastMonthMinBuy, cur.lastMonthMinSell, cur.lastMonthMaxBuy, cur.lastMonthMaxSell = getMin(2592000, key, site['id'])
				if not math.isclose(float(data['buy']),cur.buy,rel_tol=1e-11) or not math.isclose(float(data['sell']),cur.sell,rel_tol=1e-11):
					print( site['id'], key)
					cur.buy = float(data['buy'])
					cur.sell = float(data['sell'])
					cur.save()
					history = BitcoinHistory();
					history.buy = float(data['buy'])
					history.sell = float(data['sell'])
					history.currency = key
					history.timestamp = datetime.datetime.now()
					history.siteId = site['id']
					try:
						history.save()
					except Exception as e:
						print(e)
	time.sleep(30)
