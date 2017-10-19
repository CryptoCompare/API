from .models import BitcoinLiveData
from .models import BitcoinHistory
from rest_framework import serializers

class BitcoinLiveDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitcoinLiveData
        fields = ('buy', 'sell', 'lastHourMinBuy', 'lastDayMinBuy', 'lastWeekMinBuy', 'lastMonthMinBuy', 'lastHourMaxBuy', 'lastDayMaxBuy', 'lastWeekMaxBuy', 'lastMonthMaxBuy',
        	 'lastHourMinSell', 'lastDayMinSell', 'lastWeekMinSell', 'lastMonthMinSell', 'lastHourMaxSell', 'lastDayMaxSell', 'lastWeekMaxSell', 'lastMonthMaxSell', 'currency')

class BitcoinHistorySerializer(serializers.ModelSerializer):
	class Meta:
		model = BitcoinHistory
		fields = ('buy','sell','timestamp')


			
