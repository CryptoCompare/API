from .models import LiveData
from .models import ZebpayHistory
from rest_framework import serializers


class LiveDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveData
        fields = ('buy', 'sell')

class ZebpayHistorySerializer(serializers.ModelSerializer):
	class Meta:
		model = ZebpayHistory
		fields = ('buy',)
			
