from django import forms
from .models import TestCaseList

class TesetCaseCreateForm(forms.ModelForm):

    class Meta:
        model = TestCaseList
        fields = ['suite','case','task','priority','context','result']