from django.db import models

# Create your models here.


class Depertment(models.Model):
    name = models.CharField(
        verbose_name='Depertment', max_length=250, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Semester(models.Model):
    semesterChoices = [
        ('summer', 'Summer'),
        ('spring', 'Spring'),
        ('fall', 'Fall'),
    ]
    name = models.CharField(
        verbose_name='Semester',
        max_length=250,
        choices=semesterChoices,
        default=1,
    )
    num = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Program(models.Model):
    progChoices = [
        ('BA (Hons) in Fashion Design & Technology',
         'BA (Hons) in Fashion Design & Technology'),
        ('M.A. in Fashion Design', 'M.A. in Fashion Design'),
        ('BA (Hons) in Apparel Manufacturing Management & Technology',
         'BA (Hons) in Apparel Manufacturing Management & Technology'),
        ('MBA in Product & Fashion Merchandizing',
         'MBA in Product & Fashion Merchandizing'),
        ('BA (Hons) in Interior Architecture',
         'BA (Hons) in Interior Architecture'),
        ('M.A. in Interior Design', 'M.A. in Interior Design'),
        ('B. Sc (Hons) in Computer Science & Engineering',
         'B. Sc (Hons) in Computer Science & Engineering'),
        ('B. Sc (Hons) in Computer Science & Information Technology',
         'B. Sc (Hons) in Computer Science & Information Technology'),
        ('BA (Hons) in Graphic Design & Multimedia',
         'BA (Hons) in Graphic Design & Multimedia'),
        ('Bachelor of Architecture', 'Bachelor of Architecture'),
        ('BA (Hons) in Product Design', 'BA (Hons) in Product Design'),
        ('M.A. in Product Design', 'M.A. in Product Design'),
        ('achelor of Fine Arts (Hons)', 'Bachelor of Fine Arts (Hons)'),
        ('Master of Fine Arts', 'Master of Fine Arts'),
        ('Bachelor of Music (Hons) Classical, Nazrul, Rabindra Sangeet',
         'Bachelor of Music (Hons) Classical, Nazrul, Rabindra Sangeet'),
        ('Master of Music Classical, Nazrul, Rabindra Sangeet',
         'Master of Music Classical, Nazrul, Rabindra Sangeet'),
        ('Bachelor of Music (Hons) in Dance', 'Bachelor of Music (Hons) in Dance'),
        ('Master of Music in Dance', 'Master of Music in Dance'),
        ('Bachelor of Business Administration (BBA)',
         'Bachelor of Business Administration (BBA)'),
        ('Master of Business Administration (MBA)',
         'Master of Business Administration (MBA)'),
        ('Bachelor of Laws (LLB)', 'Bachelor of Laws (LLB)'),
        ('Master of Laws (LLM)', 'Master of Laws (LLM)'),
        ('BA (Hons) in English', 'BA (Hons) in English'),
        ('MA in English', 'MA in English'),
        ('BSS (Hons) in Sociology & Anthropology',
         'BSS (Hons) in Sociology & Anthropology'),
        ('MSS in Sociology & Anthropology', 'MSS in Sociology & Anthropology'),
        ('BA (Hons) in Islamic Studies', 'BA (Hons) in Islamic Studies'),
        ('MA in Islamic Studies', 'MA in Islamic Studies'),
        ('BA (Hons) in Bangla', 'BA (Hons) in Bangla'),
        ('MA in Bangla', 'MA in Bangla'),
        ('BSS (Hons) in Government & Politics',
         'BSS (Hons) in Government & Politics'),
        ('MSS in Government & Politics', 'MSS in Government & Politics'),
        ('Bachelor of Education (B. Ed.)', 'Bachelor of Education (B. Ed.)'),
    ]
    degreeChoices = [
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
    ]
    name = models.CharField(
        verbose_name='Program', max_length=250, choices=progChoices, blank=True, null=True)
    department = models.ForeignKey(Depertment, on_delete=models.PROTECT)
    degree = models.CharField(
        verbose_name='Degree Type',
        max_length=250,
        choices=degreeChoices,
        default='bachelor',
    )
    num = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Session(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)


class CourseName(models.Model):
    name = models.CharField(
        verbose_name='Course Name', max_length=250, blank=True, null=True)
    code = models.CharField(
        verbose_name='Course Code', max_length=250, blank=True, null=True)


class Course(models.Model):
    course = models.ForeignKey(CourseName, on_delete=models.PROTECT)
    program = models.ForeignKey(Program, on_delete=models.PROTECT)


# class Semester(model.models):
#     techer = 'course1' "course2"
#     student = ''
#     course = 'forein'
#     result = 'srfrser'


# depertmentChoices = [
#     (1, 'Fashion Design'),
#     (2, 'Architecture'),
#     (3, 'Computer Science'),
#     (4, 'Graphic Design & Arts'),
#     (5, 'Music & Dance'),
#     (6, 'Business'),
#     (7, 'English'),
#     (8, 'Islamic Studies'),
#     (9, 'Sociology & Politics'),
#     (10, 'Bangla'),
# ]
