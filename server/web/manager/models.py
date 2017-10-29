from django.db import models


class Temperature(models.Model):
    degree = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)


class Humidity(models.Model):
    percentage = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

# DBから過去10件の温度・湿度を取得して、乾くまでの時間をreturnする
def print_time(temperature, humidity):
    if 35<=temperature:
        sum_dry_time = 100
    elif 30<=temperature<35:
        sum_dry_time = 90
    elif 25<=temperature<30:
        sum_dry_time = 80
    elif 20<=temperature<25:
        sum_dry_time = 70
    elif 15<=temperature<20:
        sum_dry_time = 65
    elif 10<=temperature<15:
        sum_dry_time = 60
    elif 5<=temperature<10:
        sum_dry_time = 55
    elif 0<=temperature<5:
        sum_dry_time = 50
    else:
        sum_dry_time = 0

    if 0<=humidity<10:
        sum_dry_time += 100
    elif 10<=temperature<20:
        sum_dry_time += 100
    elif 20<=temperature<30:
        sum_dry_time += 90
    elif 30<=temperature<40:
        sum_dry_time += 70
    elif 40<=temperature<50:
        sum_dry_time += 50
    elif 50<=temperature<60:
        sum_dry_time += 40
    elif 60<=temperature<70:
        sum_dry_time += 30
    elif 70<=temperature<80:
        sum_dry_time += 10
    elif 80<=temperature<100:
        sum_dry_time += 0

    ave_dry_time = sum_dry_time / 2

    if 95<=ave_dry_time<100:
        superdry_time = 0
    elif 90<=ave_dry_time<95:
        superdry_time = 10
    elif 85<=ave_dry_time<90:
        superdry_time = 30
    elif 80<=ave_dry_time<85:
        superdry_time = 45
    elif 75<=ave_dry_time<80:
        superdry_time = 60
    elif 70<=ave_dry_time<75:
        superdry_time = 90
    elif 60<=ave_dry_time<70:
        superdry_time = 100
    elif 50<=ave_dry_time<60:
        superdry_time = 120
    elif 40<=ave_dry_time<50:
        superdry_time = 140
    elif 30<=ave_dry_time<40:
        superdry_time = 160
    elif 25<=ave_dry_time<30:
        superdry_time = 180


    return superdry_time


