from django.contrib import admin
from .models import Department, Semester, Session, Program
# Register your models here.


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'degree', 'department', 'num')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'num')


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Semester)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Session)