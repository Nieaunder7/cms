from django.db import models

class Department(models.Model):
    #부서명
    name = models.CharField(max_length=50)
    #코멘트
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Member(models.Model):
    #이름
    name = models.CharField(max_length=50)
    #연락처
    phone_number = models.CharField(max_length=50)
    email_address = models.EmailField()
    #부서
    department = models.ForeignKey('Department')
    #코멘트
    comment = models.CharField(max_length=200)
    #등록일 수정일
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)
    #활성
    enable = models.BooleanField(default=True)

    def __str__(self):
        return self.name

