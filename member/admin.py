from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Member, Department
# Create your views here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment']

admin.site.register(Department, DepartmentAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email_address', 'department', 'comment', 'updated', 'created', 'enable']
    list_editable = ['comment', 'enable']

admin.site.register(Member, MemberAdmin)
