from django.contrib import admin
from .models import Department, Semester, Session, Program
# Register your models here.


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'degree', 'department', 'num')

class SemesterAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'num')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'num')

class SessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'year')

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Semester,SemesterAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Session, SessionAdmin)