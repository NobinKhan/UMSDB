from django.contrib import admin
from .models import Course, CourseName, Depertment, Program, Semester, Session


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'degree', 'department', 'num')


# class SemesterAdmin(admin.ModelAdmin):
#     list_display = ('name', 'number', 'year')


admin.site.register(Depertment)
admin.site.register(Semester)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Session)
admin.site.register(CourseName)
admin.site.register(Course)
