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
from .serializers import HistorySerializer


class liveData(APIView):
		def get(self, request, siteId, currency):
			# ids = self.kwargs['siteId']
			# curr = self.kwargs['currency']
			buy = LiveData.objects.filter(siteId = siteId, currency = currency)
			serializer = LiveDataSerializer(buy, many=True)
			return Response(serializer.data)
# Create your views here.
class ZebpaHistory(APIView):
	def get(self, request, currency):
		zebpayData = ZebpayHistory.objects.filter(currency = currency)
		serializer = HistorySerializer(zebpayData, many=True)
		return Response(serializer.data)