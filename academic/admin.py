from django.contrib import admin
from .models import Depertment, Semester


class DepertmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'number')


class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'year')


admin.site.register(Depertment, DepertmentAdmin)
admin.site.register(Semester, SemesterAdmin)
