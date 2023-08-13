from manager.models import Sensor
from rest_framework import serializers


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ('pk', 'temperature', 'humidity', 'superdry_time', 'created', )
        read_only_fields = ('pk', 'superdry_time', 'created', )
