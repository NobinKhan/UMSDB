from django.contrib import admin

# Register your models here.
from app.academics.models import Department, Program, Semester


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name",)