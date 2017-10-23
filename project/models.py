from django.db import models
from member.models import Member
from device.models import BaseDevice
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name

class ProjectMember(models.Model):
    project = models.ForeignKey(Project)
    member = models.ForeignKey(Member)
    
    def __str__(self):
        return member.name

class ProjectDevice(models.Model):
    project = models.ForeignKey(Project)
    device = models.ForeignKey(BaseDevice)

    def __str__(self):
        return device.name