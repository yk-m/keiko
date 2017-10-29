from manager.models import Sensor
from rest_framework import serializers


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ('pk', 'temperature', 'humidity', 'created', )
        read_only_fields = ('pk', 'created', )
