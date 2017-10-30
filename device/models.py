from django.db import models

class BaseDevice(models.Model):
    
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=20)
    
    service = models.CharField(max_length=10)
    firmware = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    #등록일 수정일
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True, null=True)
    comment = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Settopbox(BaseDevice):
    mac_address = models.CharField(max_length=50, unique=True)

class AccessPoint(BaseDevice):
    mac_address = models.CharField(max_length=50, unique=True)

class RemoteController(BaseDevice):
    pass