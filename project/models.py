from django.db import models
from member.models import Member
from device.models import BaseDevice
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    ## 프로젝트 일정은 datetimekiper 라는 bootstrap ui 사용하면 string 으로
    ## 받아오게 되서 DateTimeField -> CharField 로 바꿈
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)
    comment = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
