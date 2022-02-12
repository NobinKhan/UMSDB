from django.db import models
from teacher.models import Teacher
from student.models import Student
from academic.models import Course, Session, Semester

# Create your models here.
dayChoice = (
    ("Saturday", 'Saturday'),
    ("Sunday", 'Sunday'),
    ("Monday", 'Monday'),
    ("Tuesday", 'Tuesday'),
    ("Wednesday", 'Wednesday'),
    ("Thursday", 'Thursday'),
    ("Friday", 'Friday'),
)

attendChoice = (
    ("absent", 'absent'),
    ("present", 'present'),
    ("validAbsent", 'validAbsent'),
)

gradeChoice = (
    ("A+", 'A+'),
    ("A", 'A'),
    ("A-", 'A-'),
    ("B+", 'B+'),
    ("B", 'B'),
    ("B-", 'B-'),
    ("C+", 'C+'),
    ("C", 'C'),
    ("C-", 'C-'),
    ("D+", 'D+'),
    ("D", 'D'),
    ("D-", 'D-'),
    ("F", 'F'),
)


class Period(models.Model):
    startTime = models.TimeField()
    endTime = models.TimeField()

    def __str__(self):
        return f"{self.startTime}-{self.endTime}"


class Shedule(models.Model):
    day = models.CharField(max_length=10, choices=dayChoice)
    period = models.ForeignKey(Period, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.day}-{self.period}"


class AssignCourse(models.Model):
    shedule = models.ManyToManyField(Shedule)
    semester = models.ForeignKey(Semester, on_delete=models.PROTECT)
    session = models.ForeignKey(Session, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    student = models.ManyToManyField(Student, blank=True)

    class Meta:
        unique_together = (('course', 'semester', 'session', 'teacher'),)

    def __str__(self):
        return f"{self.semester} {self.session} {self.course}"


class Attendance(models.Model):
    assignCourse = models.ForeignKey(
        AssignCourse, on_delete=models.PROTECT, blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attendenceDate = models.DateField(blank=True, null=True)
    attend = models.CharField(
        max_length=12, choices=attendChoice, default='absent')
    status = models.BooleanField(default='False')

    class Meta:
        unique_together = (('assignCourse', 'student', 'attendenceDate'),)

    def __str__(self):
        return f"{self.assignCourse.course} {self.student} {self.attend} {self.date}"


class CourseResult(models.Model):
    assignCourse = models.ForeignKey(
        AssignCourse, on_delete=models.PROTECT, blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    midMark = models.FloatField(
        verbose_name='Midterm Mark', blank=True, null=True)
    finalMark = models.FloatField(
        verbose_name='Final Mark', blank=True, null=True)
    creditHours = models.FloatField(
        verbose_name='Credit Hours', blank=True, null=True)
    gradePoint = models.FloatField(
        verbose_name='Grade Point', blank=True, null=True)
    grade = models.CharField(
        max_length=12, choices=gradeChoice, default='F')
    midDate = models.DateTimeField(auto_now_add=True)
    finalDate = models.DateTimeField(auto_now_add=True)
    lastEditDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('assignCourse', 'student'),)

    def __str__(self):
        return f"{self.assignCourse.course} {self.student} {self.attend} {self.date}"


class SemResult(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.PROTECT)
    session = models.ForeignKey(Session, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    totalCredit = models.FloatField(
        verbose_name='Total Credit', blank=True, null=True)
    earnedCredit = models.FloatField(
        verbose_name='Earned Credit', blank=True, null=True)
    sgpa = models.FloatField(verbose_name='SGPA', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    lastEditDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('semester', 'session', 'student'),)

    def __str__(self):
        return f"{self.assignCourse.course} {self.student} {self.attend} {self.date}"
