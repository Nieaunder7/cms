from django.shortcuts import render, redirect
from project.models import Project
from .forms import ProjectForm
import logging

logger = logging.getLogger(__name__)

def project_list(request):
    projects = Project.objects.all()
    param = {
        'title':"프로젝트 리스트", 
        'projects':projects
        }
    return render(request, 'project_list.html', param)

def project_add(request):
    logger.error("project_add")
    if request.method == "POST":
        logger.error("POST")
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project_form.save()
            return redirect('project:project_list')
        else :
            logger.error("not is_valid()")
            return redirect('project:project_list')
    else :
        project_form = ProjectForm()
        return render(request,'project_form.html',{'project_form':project_form})