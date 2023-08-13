from django.conf.urls import include, url
from rest_framework import routers

from .views import SensorViewSet

router = routers.SimpleRouter()
router.register(r'sensor', SensorViewSet, base_name="sensor")

urlpatterns = router.urls
