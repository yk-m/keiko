from django.shortcuts import render
from manager.models import Humidity, Temperature
from rest_framework import viewsets

from .serializer import HumiditySerializer, TemperatureSerializer


class TemperatureViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer


class HumidityViewSet(viewsets.ModelViewSet):
    queryset = Humidity.objects.all()
    serializer_class = HumiditySerializer
