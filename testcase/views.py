from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import TestCaseList
from .forms import TesetCaseCreateForm
import logging

logger = logging.getLogger(__name__)

@login_required
def testCase_list(request):
    testcase = TestCaseList.objects.all()
    param = {
        'title':"테스트현황",
        'testcase':testcase
    }
    return render(request,'testcase_list.html',param)

@login_required
def testcase_add(request):
    if request.method == "POST":
        form = TesetCaseCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testcase:testcase_list')
    else :
        form = TesetCaseCreateForm()
        return render(request,'testcase_form.html',{'form':form})


@login_required
def testcase_update(request,pk):
    model = get_object_or_404(TestCaseList,pk=pk)
    if request.method == "POST":
        form = TesetCaseCreateForm(request.POST,instance=model)
        if form.is_valid():
            form.save()
            return redirect("testcase:testcase_list")
    else :
        form = TesetCaseCreateForm(instance=model)
        return render(request,'testcase_form.html',{'form':form})

@login_required
def testcase_delete(request,pk):
    TestCaseList.objects.filter(pk=pk).delete()
    return redirect('testcase:testcase_list')