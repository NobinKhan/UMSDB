from django.contrib import admin

from teacher.models import Teacher

# Register your models here.


class TeacherAdmin(admin.ModelAdmin):
    readonly_fields = ['uid']


admin.site.register(Teacher, TeacherAdmin)
