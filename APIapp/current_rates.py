import requests as r

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

data = {
	"success": False,
	"buy": -1,
	"sell": -1,
	"volume": -1
}

def getRate(apiInfo):
	if(len(apiInfo)>0):
		if 'all' in apiInfo:
			api = apiInfo['all']
			if 'volumeKey' in apiInfo:
				sendRequest(api['endpoint'], api['buyKey'], api['sellKey'], api['volumeKey'])
			else:
				sendRequest(api['endpoint'], api['buyKey'], api['sellKey'], -1)
			print data
		else :
			apiBuy = apiInfo['buy']
			sendRequest(apiBuy['endpoint'], apiBuy['buyKey'], -1, -1)

			apiSell = apiInfo['sell']
			sendRequest(apiSell['endpoint'], -1, apiSell['sellKey'], -1)

			if 'volume' in apiInfo:
				apiVolume = apiInfo['volume']
				sendRequest(apiVolume['endpoint'], -1, -1, apiVolume['volumeKey'])
			print data



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

# url = "https://api.coinbase.com/v2/prices/sell?currency=SGD"
# buyKey = "data.amount"
# sellKey = "data.currency"
# volumeKey = "data.currency"
# sendRequest(url, buyKey, sellKey, volumeKey)
