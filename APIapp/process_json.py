import json
import current_rates

filename = "exchanges.json"

try:
	f = open(filename, 'r')
	json_data = json.loads(f.read())
	for key, value in json_data.iteritems():
			for site in value:
				print site['id'], " : ", key, " - ", site['name']
				current_rates.getRate(site['api'])
	f.close()
except IOError:
	print 'problem reading: ' + filename
