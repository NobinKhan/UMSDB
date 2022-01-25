from django.db import models
from core.models import User

# Create your models here.


class Student(models.Models):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
