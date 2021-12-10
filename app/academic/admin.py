from django.contrib import admin
from app.academic.models import Department, Program, Semester
# Register your models here.


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Program)

admin.site.register(Semester)