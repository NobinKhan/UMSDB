from django.db import models

# Create your models here.


class Depertment(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(blank=False)

    def __str__(self):
        return self.name


class Semester(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(blank=False)
    year = models.IntegerField()

    def __str__(self):
        return str(self.year) + ' ' + str(self.name)
