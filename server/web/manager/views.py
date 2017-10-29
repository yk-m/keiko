from django.shortcuts import render

from .models import Sensor


# DBから過去10件の温度と湿度を取得して、その値からsuperdryの時間をテンプレートに渡す
def print_time(request):
    sensor = Sensor.objects.order_by('-created').first()
    if sensor is None:
        return render(request, 'default.html')
    return render(request, 'print_time.html', {"sensor": sensor})
