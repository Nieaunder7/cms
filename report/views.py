from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from report.models import BaseReport

@login_required
def report_list(request):
    reports = BaseReport.objects.all()
    param = {
        'title':"리포트 리스트", 
        'reports':reports
        }
    return render(request, 'report_list.html', param)