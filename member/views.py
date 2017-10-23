from django.shortcuts import render
from .models import Member, Department

def member_list(request):
    title = "멤버리스트"
    members = Member.objects.all()
    return render(request, 'member_list.html', {'page_title':title, 'members':members})