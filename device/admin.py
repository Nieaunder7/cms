from django.contrib import admin
from .models import Settopbox, AccessPoint, RemoteController
# Create your views here.

class SettopboxAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'model',
        'mac_address',
        'manufacturer',
        'service',
        'firmware',
        'created',
        'updated',
        'comment'
    ]

admin.site.register(Settopbox, SettopboxAdmin)

class AccessPointAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'model',
        'mac_address',
        'manufacturer',
        'service',
        'firmware',
        'created',
        'updated',
        'comment'
    ]

admin.site.register(AccessPoint, AccessPointAdmin)

class RemoteControllerAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'model',
        'manufacturer',
        'service',
        'firmware',
        'created',
        'updated',
        'comment'
    ]

admin.site.register(RemoteController, RemoteControllerAdmin)
