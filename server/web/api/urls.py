from django.conf.urls import include, url
from rest_framework import routers

from .views import HumidityViewSet, TemperatureViewSet

router = routers.SimpleRouter()
router.register(r'temperature', TemperatureViewSet, base_name="temperature")
router.register(r'humidity', HumidityViewSet, base_name="humidity")

urlpatterns = router.urls
