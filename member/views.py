from django.shortcuts import render, redirect, get_object_or_404
from .models import Member, Department
from .forms import MemberCreateForm

import logging

logger = logging.getLogger(__name__)

def member_list(request):
    members = Member.objects.all()
    param = {
        'title':"멤버리스트", 
        'members':members
        }
    return render(request, 'member_list.html', param)

def member_add(request):
    if request.method == "POST":
        form = MemberCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member:member_list')
    else :
        form = MemberCreateForm()
        return render(request, 'member_form.html',{'form':form})

## 회원 수정
def member_update(request,pk):
    model = get_object_or_404(Member,pk=pk)
    if request.method == "POST":
        form = MemberCreateForm(request.POST,instance=model)
        if form.is_valid():
            form.save()
            return redirect('member:member_list')
    else :
        form = MemberCreateForm(instance=model)
        return render(request,'member_form.html',{'form':form})

def member_delete(request,pk):
    member = Member.objects.filter(pk=pk).delete()
    return redirect('member:member_list')

