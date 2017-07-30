from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import LiveData
from .serializers import LiveDataSerializer
from rest_framework import generics
from .models import LiveData
from .models import ZebpayHistory
from .serializers import ZebpayHistorySerializer
from .serializers import CoinbaseHistorySerializer
from .serializers import CoinhakoHistorySerializer
import datetime
from datetime import timedelta
import json


class liveData(APIView):
	def get(self, request):
		# ids = self.kwargs['siteId']
		# curr = self.kwargs['currency']
		response = {}
		site = ['Zebpay', 'Coinbase', 'Coinhako']
		siteId = request.GET.getlist('siteId')
		currency = request.GET.getlist('currency')
		for i in range(len(siteId)):
			buy = LiveData.objects.filter(siteId = siteId[i], currency = currency[i])
			serializer = LiveDataSerializer(buy, many=True)
			response[site[int(siteId[i])-1]] = serializer.data
		#response_json = json.dumps(response)
		return Response(response)
# Create your views here.
class History(APIView):
	def get(self, request, siteId, currency, time):
		response = Response()
		if int(siteId) == 1:
			time_threshold = datetime.datetime.now() - timedelta(seconds = int(time))
			data = ZebpayHistory.objects.filter(currency = request.GET['currency'], timestamp__range=(time_threshold,datetime.datetime.now()))
			serializer = ZebpayHistorySerializer(data, many=True)
			response = Response(serializer.data)
		elif int(siteId) == 2:
			time_threshold = datetime.datetime.now() - timedelta(seconds = int(time))
			data = CoinbaseHistory.objects.filter(currency = request.GET['currency'], timestamp__range=(time_threshold,datetime.datetime.now()))
			serializer = CoinbaseHistorySerializer(data, many=True)
			response = Response(serializer.data)
		elif int(siteId) == 3:
			time_threshold = datetime.datetime.now() - timedelta(seconds = int(time))
			data = CoinhakoHistory.objects.filter(currency = request.GET['currency'], timestamp__range=(time_threshold,datetime.datetime.now()))
			serializer = CoinhakoHistorySerializer(data, many=True)
			response = Response(serializer.data)
		#print (datetime.datetime.now() - response['timestamp'])
		return response