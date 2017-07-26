from .models import LiveData
from .models import ZebpayHistory
from .models import CoinhakoHistory
from .models import CoinbaseHistory
from rest_framework import serializers


class LiveDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveData
        fields = ('buy', 'sell')

class HistorySerializer(serializers.ModelSerializer):
	class Meta:
		model = ZebpayHistory
		fields = ('buy','sell','timestamp')

			
