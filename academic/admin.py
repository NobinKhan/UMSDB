from django.contrib import admin
from .models import Course, Attendance, AssignCourse, CourseResult, Period, SemResult, Shedule, AttendanceStatus, CourseStatus

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


@admin.register(CourseStatus)
class CourseStatusAdmin(admin.ModelAdmin):
    list_display=('id','assignCourse','student','retake')


@admin.register(CourseResult)
class CourseResultAdmin(admin.ModelAdmin):
    readonly_fields = ['midAddDate', 'midLastEditDate','finalAddDate', 'finalLastEditDate']
    list_display=('id','assignCourse','student','grade')


@admin.register(SemResult)
class SemResultAdmin(admin.ModelAdmin):
    readonly_fields = ['sgpa', 'totalCredit','earnedCredit', 'date']
    list_display=('id','semester','session','student','sgpa')

