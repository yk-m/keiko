from manager.models import Humidity, Temperature
from rest_framework import serializers


class TemperatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Temperature
        fields = ('pk', 'degree', 'created', )
        read_only_fields = ('pk', 'created', )


class HumiditySerializer(serializers.ModelSerializer):

    class Meta:
        model = Humidity
        fields = ('pk', 'percentage', 'created', )
        read_only_fields = ('pk', 'created', )
