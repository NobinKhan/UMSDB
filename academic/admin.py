from django.contrib import admin
from .models import Course, Attendance, AssignCourse, CourseResult, Period, SemResult, Shedule, AttendanceStatus

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


@admin.register(AttendanceStatus)
class AttendanceStatusAdmin(admin.ModelAdmin):
    list_display=('id','attendance','student','status')


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display=('id','assignCourse','attendenceDate')


@admin.register(AssignCourse)
class AssignCourseAdmin(admin.ModelAdmin):
    list_display=('id','semester','session','course','teacher')


@admin.register(CourseResult)
class CourseResultAdmin(admin.ModelAdmin):
    readonly_fields = ['midAddDate', 'midLastEditDate','finalAddDate', 'finalLastEditDate']
    list_display=('id','assignCourse','student','grade')



admin.site.register(SemResult)


# class SemesterAdmin(admin.ModelAdmin):
#     list_display = ('name', 'number', 'year')



