import requests as r
import json
import os
import schedule
import time
import datetime
from coinbase.wallet.client import Client
import math
import json
from pprint import pprint

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
response_data = {
	"currency": "CUR",
	"id": -1,
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
			data1.lastHourMin = -1;
			data1.lastDayMin = -1;
			data1.lastWeekMin = -1;
			data1.lastMonthMin = -1;
			data1.lastHourMax = -1;
			data1.lastDayMax = -1;
			data1.lastWeekMax = -1;
			data1.lastMonthMax = -1;
			data1.save()

except IOError:
	print ('problem reading: ' + filename)

while 1:
	for key, value in json_data.items():
			for site in value:
				getRate(site['api'])
				response_data["currency"] = key
				response_data["id"] = site['id']
#				response_data["success"] = data["success"]
				response_data["buy"] = data["buy"]
				response_data["sell"] = data["sell"]
				response_data["volume"] = data["volume"]
				cur = BitcoinLiveData.objects.get(siteId = site['id'], currency = key)
				if not math.isclose(float(response_data['buy']),cur.buy,rel_tol=1e-11) or not math.isclose(float(response_data['sell']),cur.sell,rel_tol=1e-11):
					cur.buy = data['buy']
					cur.sell = data['sell']
					cur.save()
					history = BitcoinHistory();
					history.buy = data['buy']
					history.sell = data['sell']
					history.currency = key
					history.timestamp = datetime.datetime.now()
					history.siteId = site['id']
					try:
						print(history.siteId)
						history.save()
					except Exception as e:
						print(e)
	time.sleep(30)
