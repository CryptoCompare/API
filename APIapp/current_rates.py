import requests as r

"""
API will contain 1, 2 or 3 fields in the JSON file

One: all the values exist in one JSON, volume will be null, if not provided by the API
Two: buy, sell, volume is not provided by the API
Three: if at least two of the three things(buy, sell, volume) differ


Validate in current_rates.py if volume is provided or not
"""

data = {
	"buy": -1,
	"sell": -1,
	"volume": -1
}
def getRate(url, buyKey, sellKey, volumeKey):
	response = r.get(url)
	responseJson = response.json()

	buyKey = buyKey.split('.')
	sellKey = sellKey.split('.')
	volumeKey = volumeKey.split('.')

	val = responseJson
	for key in buyKey:
		val = val[key]
	data['buy'] = val

	val = responseJson
	for key in sellKey:
		val = val[key]
	data['sell'] = val

	val = responseJson
	for key in volumeKey:
		val = val[key]
	data['volume'] = val

	print data

url = "https://api.coinbase.com/v2/prices/sell?currency=SGD"
buyKey = "data.amount"
sellKey = "data.currency"
volumeKey = "data.currency"
getRate(url, buyKey, sellKey, volumeKey)
