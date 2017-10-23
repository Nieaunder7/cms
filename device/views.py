from django.shortcuts import render
from .models import BaseDevice, Settopbox, AccessPoint, RemoteController

def device_list(request):
    devices = BaseDevice.objects.all()
    param = {
        'title':"장치 리스트", 
        'devices':devices
        }
    return render(request, 'device_list.html', param)