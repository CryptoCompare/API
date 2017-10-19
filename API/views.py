from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import BitcoinLiveDataSerializer
from rest_framework import generics
from .models import BitcoinLiveData
from .models import BitcoinHistory
from .serializers import BitcoinHistorySerializer
import datetime
from datetime import timedelta
import json


class liveData(APIView):
	def post(self, request):
		# ids = self.kwargs['siteId']
		# curr = self.kwargs['currency']
		response = {}
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		filename = "included_sites.json"
		try :
			f = open(filename, 'r')
			json_data = json.loads(f.read())
			site = [None]*(len(json_data)+1)
			for key, value in json_data.items():
				site[int(value['id'])-1] = key
			for cryptoCurrency in body:
			#	print(cryptoCurrency, " ")
				for currency in body[cryptoCurrency]:
			#		print(currency , " ")
					for siteId in body[cryptoCurrency][currency]:
			#			print(siteId, " ")
						buy = BitcoinLiveData.objects.filter(siteId = siteId, currency = currency)
						serializer = BitcoinLiveDataSerializer(buy, many=True)
						if site[int(siteId)-1] in response:
							response[site[int(siteId)-1]].append(serializer.data)
						else:
							response[site[int(siteId)-1]] = [serializer.data]
		except Exception as e:
			print(e)
		#response_json = json.dumps(response)
		return Response(response)
# Create your views here.
class history(APIView):
	def post(self, request):
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		response = {}
		site = []
		filename = "included_sites.json"
		try:
			f = open(filename, 'r')
			json_data = json.loads(f.read())
			site = [None]*(len(json_data)+1)
			for key, value in json_data.items():
				site[int(key)-1] = value
			for cryptoCurrency in body:
				for currency in body[cryptoCurrency]:
					for siteData in body[cryptoCurrency][currency]:
						print(siteData['id'])
						time_threshold = datetime.datetime.now() - timedelta(seconds = int(siteData['timestamp']))
						data = BitcoinHistory.objects.filter(currency = currency, siteId = siteData['id'], timestamp__range=(time_threshold,datetime.datetime.now()))
						serializer = BitcoinHistorySerializer(data, many=True)
						response[site[int(siteData['id'])-1]] = serializer.data

		except Exception as e:
			print(e)
		return Response(response)