from django.contrib import admin
from .models import Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ['uid']


admin.site.register(Student, StudentAdmin)
