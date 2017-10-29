from django.shortcuts import render
from .models import print_time

# DBから過去10件の温度と湿度を取得して、その値からsuperdryの時間をテンプレートに渡す
def print_time():
    temperature = Temperature.object.order_by('-created')[:1][0]
    humidity = Humidity.object.order_by('-created')[:1][0]
    superdry_time = print_time(temperature, humidity)
    return render(request, 'print_time.html', superdry_time)
