from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name','start_date','end_date','comment']

# class ProjectDeviceForm(forms.ModelForm):

#     class Meta:
#         model = ProjectDevice
#         fields = ['device']

# class ProjectMemberForm(forms.ModelForm):

#     class Meta:
#         model = ProjectMember
#         fields = ['member']
