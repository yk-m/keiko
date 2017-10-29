from django.db import models


class Sensor(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
