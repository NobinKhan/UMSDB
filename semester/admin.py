from ast import Assign
from django.contrib import admin
from .models import Attendance, AssignCourse, CourseResult, Period, SemResult, Shedule
# Register your models here.
admin.site.register(Period)
admin.site.register(Shedule)
admin.site.register(AssignCourse)
admin.site.register(Attendance)
admin.site.register(CourseResult)
admin.site.register(SemResult)
