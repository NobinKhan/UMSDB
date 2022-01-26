from statistics import mode
from django.db import models

# Create your models here.


class Depertment(models.Model):
    depertmentChoices = [
        (1, 'Fashion Design'),
        (2, 'Architecture'),
        (3, 'Computer Science'),
        (4, 'Graphic Design & Arts'),
        (5, 'Music & Dance'),
        (6, 'Business'),
        (7, 'English'),
        (8, 'Islamic Studies'),
        (9, 'Sociology & Politics'),
        (10, 'Bangla'),
    ]
    name = models.CharField(
        verbose_name='Depertment',
        max_length=2,
        choices=depertmentChoices,
        default=1,
    )
    def __str__(self):
        return str(self.name)


class Semester(models.Model):
    semesterChoices = [
        (1, 'Summer'),
        (2, 'Spring'),
        (3, 'Fall'),
    ]
    name = models.CharField(
        verbose_name='Semester',
        max_length=2,
        choices=semesterChoices,
        default=1,
    )

    def __str__(self):
        return str(self.name)


class Program(models.Model):
    progChoices = [
        (0, 'None'),
        (1, 'BA (Hons) in Fashion Design & Technology'),
        (2, 'M.A. in Fashion Design'),
        (3, 'BA (Hons) in Apparel Manufacturing Management & Technology'),
        (4, 'MBA in Product & Fashion Merchandizing'),
        (5, 'BA (Hons) in Interior Architecture'),
        (6, 'M.A. in Interior Design'),
        (7, 'B. Sc (Hons) in Computer Science & Engineering'),
        (8, 'B. Sc (Hons) in Computer Science & Information Technology'),
        (9, 'BA (Hons) in Graphic Design & Multimedia'),
        (10, 'Bachelor of Architecture'),
        (11, 'BA (Hons) in Product Design'),
        (12, 'M.A. in Product Design'),
        (13, 'Bachelor of Fine Arts (Hons)'),
        (14, 'Master of Fine Arts'),
        (15, 'Bachelor of Music (Hons) Classical, Nazrul, Rabindra Sangeet'),
        (16, 'Master of Music Classical, Nazrul, Rabindra Sangeet'),
        (17, 'Bachelor of Music (Hons) in Dance'),
        (18, 'Master of Music in Dance'),
        (19, 'Bachelor of Business Administration (BBA)'),
        (20, 'Master of Business Administration (MBA)'),
        (21, 'Bachelor of Laws (LLB)'),
        (22, 'Master of Laws (LLM)'),
        (23, 'BA (Hons) in English'),
        (24, 'MA in English'),
        (25, 'BSS (Hons) in Sociology & Anthropology'),
        (26, 'MSS in Sociology & Anthropology'),
        (27, 'BA (Hons) in Islamic Studies'),
        (28, 'MA in Islamic Studies'),
        (29, 'BA (Hons) in Bangla'),
        (30, 'MA in Bangla'),
        (31, 'BSS (Hons) in Government & Politics'),
        (32, 'MSS in Government & Politics'),
        (33, 'Bachelor of Education (B. Ed.)'),
    ]
    name = models.CharField(
        verbose_name='Program',
        max_length=2,
        choices=progChoices,
        default=0,
    )

    def __str__(self):
        return str(self.name)


class Session(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)


class Degree(models.Model):
    degreeChoices = [
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
    ]
    name = models.CharField(
        verbose_name='Degree Type',
        max_length=2,
        choices=degreeChoices,
        default='bachelor',
    )

    def __str__(self):
        return str(self.name)
