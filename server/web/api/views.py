from django.shortcuts import render
from manager.models import Sensor
from rest_framework import viewsets

from .serializer import SensorSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
