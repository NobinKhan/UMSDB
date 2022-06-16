from django.contrib import admin
from .models import Course, Attendance, AssignCourse, CourseResult, Period, SemResult, Shedule

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=('id','code','name','department')


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display=('id','startTime','endTime')

@admin.register(Shedule)
class SheduleAdmin(admin.ModelAdmin):
    list_display=('id','day','period')



admin.site.register(AssignCourse)
admin.site.register(Attendance)
admin.site.register(CourseResult)
admin.site.register(SemResult)



# class SemesterAdmin(admin.ModelAdmin):
#     list_display = ('name', 'number', 'year')



