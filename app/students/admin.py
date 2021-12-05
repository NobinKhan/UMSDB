from django.contrib import admin

# Register your models here.
from app.students.models import Student


admin.site.register(Student)