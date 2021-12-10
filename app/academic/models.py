from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=255, null=True)
    department_code = models.PositiveBigIntegerField(null=True)
    created_at = models.DateTimeField('date time created at', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('date time updated at', auto_now=True, null=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=255, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField('date time created at', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('date time updated at', auto_now=True, null=True)


class Semester(models.Model):
    name = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField('date time created at', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('date time updated at', auto_now=True, null=True)


class Batch(models.Model):
    batch_number = models.PositiveBigIntegerField(null=True)
    created_at = models.DateTimeField('date time created at', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('date time updated at', auto_now=True, null=True)