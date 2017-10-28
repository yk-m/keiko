from django.db import models


class Temperature(models.Model):
    degree = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)


class Humidity(models.Model):
    percentage = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
