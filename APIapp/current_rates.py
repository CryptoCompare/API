import requests as r

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