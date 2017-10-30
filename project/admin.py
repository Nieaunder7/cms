from django.contrib import admin
from .models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display=['name','start_date','end_date','comment']

admin.site.register(Project,ProjectAdmin)