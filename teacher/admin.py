from django.contrib import admin

from teacher.models import Teacher

# Register your models here.


class TeacherAdmin(admin.ModelAdmin):
    readonly_fields = ['uid']
    list_display=('id','uid')


admin.site.register(Teacher, TeacherAdmin)
