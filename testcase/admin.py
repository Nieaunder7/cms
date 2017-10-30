from django.contrib import admin
from .models import TestCaseList
# Register your models here.

class TestCaseListAdmin(admin.ModelAdmin):
    list_display = [
        'suite', 'case','task','priority','context','result'
    ]

admin.site.register(TestCaseList,TestCaseListAdmin)