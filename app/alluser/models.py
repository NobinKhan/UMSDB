from django.core.validators import BaseValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from app.academic.models import Department, Program
# Create your models here.


class Blood(models.Model):
    blood_group = models.CharField(max_length=3, null=True)
    created_at = models.DateTimeField('date time created at', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('date time updated at', auto_now=True, null=True)

    def __str__(self):
        return self.blood_group


class Designation(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField('date time created at', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('date time updated at', auto_now=True, null=True)

    def __str__(self):
        return self.title


class AllUser(AbstractUser):
    gender = (
        ("Male", "Male"), ("Female", "Female"), ("3rd Gender", "3rd Gender"),
    )
    user_id = models.CharField(max_length=50, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.IntegerField(max_length=14, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=gender, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    blood_group = models.ForeignKey(Blood, on_delete=models.CASCADE, null=True, blank=True)
    guardian_name = models.CharField(max_length=100, null=True, blank=True)
    guardian_phone = models.IntegerField(max_length=14, null=True, blank=True)
    guardian_email = models.EmailField(max_length=100, null=True, blank=True)
    present_address = models.TextField(null=True, blank=True)
    permanent_address = models.TextField(null=True, blank=True)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, null=True, blank=True)
    starting_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='uploads/user')
    created_at = models.DateTimeField('date time created at', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('date time updated at', auto_now=True, null=True)
