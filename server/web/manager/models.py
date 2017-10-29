from django.db import models
from django.utils.functional import cached_property


class Sensor(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    @cached_property
    def superdry_time(self):
        """乾くまでの推定時間"""

        if 35 <= self.temperature:
            sum_dry_time = 100
        elif 30 <= self.temperature:
            sum_dry_time = 90
        elif 25 <= self.temperature:
            sum_dry_time = 80
        elif 20 <= self.temperature:
            sum_dry_time = 70
        elif 15 <= self.temperature:
            sum_dry_time = 65
        elif 10 <= self.temperature:
            sum_dry_time = 60
        elif 5 <= self.temperature:
            sum_dry_time = 55
        elif 0 <= self.temperature:
            sum_dry_time = 50
        else:
            sum_dry_time = 0

        if 0 <= self.humidity:
            sum_dry_time += 100
        elif 10 <= self.humidity:
            sum_dry_time += 100
        elif 20 <= self.humidity:
            sum_dry_time += 90
        elif 30 <= self.humidity:
            sum_dry_time += 70
        elif 40 <= self.humidity:
            sum_dry_time += 50
        elif 50 <= self.humidity:
            sum_dry_time += 40
        elif 60 <= self.humidity:
            sum_dry_time += 30
        elif 70 <= self.humidity:
            sum_dry_time += 10
        elif 80 <= self.humidity:
            sum_dry_time += 0

        ave_dry_time = sum_dry_time / 2

        if 95 <= ave_dry_time:
            superdry_time = 0
        elif 90 <= ave_dry_time:
            superdry_time = 10
        elif 85 <= ave_dry_time:
            superdry_time = 30
        elif 80 <= ave_dry_time:
            superdry_time = 45
        elif 75 <= ave_dry_time:
            superdry_time = 60
        elif 70 <= ave_dry_time:
            superdry_time = 90
        elif 60 <= ave_dry_time:
            superdry_time = 100
        elif 50 <= ave_dry_time:
            superdry_time = 120
        elif 40 <= ave_dry_time:
            superdry_time = 140
        elif 30 <= ave_dry_time:
            superdry_time = 160
        elif 25 <= ave_dry_time:
            superdry_time = 180

        return superdry_time
