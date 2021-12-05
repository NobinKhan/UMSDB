from django.db import models
from app.academics.models import Department, Program

# Create your models here.

class Student(models.Model):
    student_id = models.PositiveBigIntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True)
    # cgpa = models
    email = models.EmailField(max_length=100, null=True)
    phone = models.IntegerField(max_length=14, null=True)
    date_of_birth = models.DateTimeField(null=True)
    blood_group = models.CharField(max_length=3, null=True)
    guardian_name = models.CharField(max_length=100, null=True)
    guardian_phone = models.IntegerField(max_length=14, null=True)
    guardian_email = models.EmailField(max_length=100, null=True)
    present_address = models.TextField(null=True)
    permanent_address = models.TextField(null=True)
