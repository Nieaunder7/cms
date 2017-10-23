from django.shortcuts import render
from project.models import Project

def project_list(request):
    projects = Project.objects.all()
    param = {
        'title':"프로젝트 리스트", 
        'projects':projects
        }
    return render(request, 'project_list.html', param)