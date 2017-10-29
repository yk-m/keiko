from django.shortcuts import render
from .models import print_time,Temperature,Humidity



# DBから過去10件の温度と湿度を取得して、その値からsuperdryの時間をテンプレートに渡す
def print_time(request):
    temperature = Temperature.objects.order_by('-created')[:1]
    humidity = Humidity.objects.order_by('-created')[:1]
    superdry_time = print_time(temperature, humidity)
    return render(request, 'print_time.html', {"superdry_time": superdry_time})
