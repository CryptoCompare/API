from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import LiveData
from .serializers import LiveDataSerializer
from rest_framework import generics
from .models import LiveData
from .models import History
from .serializers import HistorySerializer
import datetime
from datetime import timedelta
import json


class liveData(APIView):
	def get(self, request):
		# ids = self.kwargs['siteId']
		# curr = self.kwargs['currency']
		response = {}
		site = []
		filename = "included_sites.json"
		try :
			f = open(filename, 'r')
			json_data = json.loads(f.read())
			for key, value in json_data.items():
				site.append(value)
			siteId = request.GET.getlist('siteId')
			currency = request.GET.getlist('currency')
			for i in range(len(siteId)):
				buy = LiveData.objects.filter(siteId = siteId[i], currency = currency[i])
				serializer = LiveDataSerializer(buy, many=True)
				response[site[int(siteId[i])-1]] = serializer.data
				print("g")
				print(serializer.data)
		except Exception as e:
			print(e)
		#response_json = json.dumps(response)
		return Response(response)
# Create your views here.
class history(APIView):
	def get(self, request, siteId, currency, time):
		response = Response()
		time_threshold = datetime.datetime.now() - timedelta(seconds = int(time))
		print(time_threshold)
		data = History.objects.filter(currency = currency, siteId = siteId, timestamp__range=(time_threshold,datetime.datetime.now()))
		serializer = HistorySerializer(data, many=True)
		response = Response(serializer.data)
		return response