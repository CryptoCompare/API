from .models import LiveData
from .models import History
from rest_framework import serializers

class LiveDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveData
        fields = ('buy', 'sell')

class HistorySerializer(serializers.ModelSerializer):
	class Meta:
		model = History
		fields = ('buy','sell','timestamp')


			
