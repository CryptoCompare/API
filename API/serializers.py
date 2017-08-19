from .models import BitcoinLiveData
from .models import BitcoinHistory
from rest_framework import serializers

class BitcoinLiveDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitcoinLiveData
        fields = ('buy', 'sell', 'lastHourMin', 'lastDayMin', 'lastWeekMin', 'lastMonthMin', 'lastHourMax', 'lastDayMax', 'lastWeekMax', 'lastMonthMax')

class BitcoinHistorySerializer(serializers.ModelSerializer):
	class Meta:
		model = BitcoinHistory
		fields = ('buy','sell','timestamp')


			
