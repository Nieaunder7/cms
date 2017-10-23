from django.shortcuts import render
from .models import Member, Department

def member_list(request):
    members = Member.objects.all()
    param = {
        'title':"멤버리스트", 
        'members':members
        }
    return render(request, 'member_list.html', param)