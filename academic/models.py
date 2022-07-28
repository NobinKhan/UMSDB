from django.db import models
from django.conf import settings
from django.utils import timezone
from layouts.models import Program, Semester, Session, Department
# Create your models here.



class Course(models.Model):
    name = models.CharField(
        verbose_name='Course Name', unique=True, max_length=100, blank=True, null=True)
    code = models.CharField(
        verbose_name='Course Code',unique=True, max_length=20, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, blank=True, null=True)
    program = models.ManyToManyField(Program)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                # conditions=Q(is_active=True),
                fields=["name", "code"],
                name="unique_course"
            )
        ]

    def __str__(self):
        return f"{self.code} {self.name}"


class Period(models.Model):
    startTime = models.TimeField()
    endTime = models.TimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["startTime", "endTime"],
                name="unique_Class_Time"
            )
        ]

    def __str__(self):
        return f"{self.startTime}-{self.endTime}"


class Shedule(models.Model):
    dayChoice = (
    ("Saturday", 'Saturday'),
    ("Sunday", 'Sunday'),
    ("Monday", 'Monday'),
    ("Tuesday", 'Tuesday'),
    ("Wednesday", 'Wednesday'),
    ("Thursday", 'Thursday'),
    ("Friday", 'Friday'),
    )
    day = models.CharField(max_length=10, choices=dayChoice)
    period = models.ForeignKey(Period, on_delete=models.PROTECT)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["day", "period"],
                name="unique_Shedule"
            )
        ]

    def __str__(self):
        return f"{self.day}-{self.period}"


class AssignCourse(models.Model):
    shedule = models.ManyToManyField(Shedule)
    semester = models.ForeignKey(Semester, on_delete=models.PROTECT)
    session = models.ForeignKey(Session, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,related_name="Teacher",)
    student = models.ManyToManyField(settings.AUTH_USER_MODEL, through='RetakeCourse', blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['course', 'semester', 'session', 'teacher'],
                name="unique_AssignCourse"
            )
        ]

    def __str__(self):
        return f"{self.semester} {self.session} {self.course}"


class RetakeCourse(models.Model):
    assignCourse = models.ForeignKey(AssignCourse, on_delete=models.PROTECT)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    retake = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['assignCourse', 'student', 'retake'],
                name="unique_RetakeCourse"
            )
        ]

    def __str__(self):
        return f"{self.assignCourse} {self.student} {self.retake}"


class Attendance(models.Model):
    assignCourse = models.ForeignKey(
        AssignCourse, on_delete=models.PROTECT, blank=True, null=True)
    attendenceDate = models.DateField(blank=True, null=True)
    shedule = models.ForeignKey(Shedule, on_delete=models.PROTECT)
    student = models.ManyToManyField(settings.AUTH_USER_MODEL, through='AttendanceStatus')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                # conditions=Q(is_active=True),
                fields=['assignCourse', 'attendenceDate','shedule'],
                name="unique_attendance"
            )
        ]

    def __str__(self):
        return f"{self.assignCourse.course}  {self.attendenceDate}"


class AttendanceStatus(models.Model):
    attendanceChoices = (
    ("Present", 'Present'),
    ("Absent", 'Absent'),
    ("AbsentOnLeave", 'AbsentOnLeave'),
    )
    attendance = models.ForeignKey(Attendance, on_delete=models.PROTECT)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    status = models.CharField(max_length=15, choices=attendanceChoices)
    class Meta:
        verbose_name = "Attendance Status"
        constraints = [
            models.UniqueConstraint(
                # conditions=Q(is_active=True),
                fields=['attendance', 'student'],
                name="unique_attendanceStatus"
            )
        ]

    def __str__(self):
        return f"{self.attendance}  {self.student} {self.status}"


class CourseResult(models.Model):
    gradeChoice = (
        ("A+", 'A+'),
        ("A", 'A'),
        ("A-", 'A-'),
        ("B+", 'B+'),
        ("B", 'B'),
        ("B-", 'B-'),
        ("C+", 'C+'),
        ("C", 'C'),
        ("D", 'D'),
        ("AB", 'AB'),
        ("F", 'F'),
    )
    assignCourse = models.ForeignKey(
        AssignCourse, on_delete=models.PROTECT, blank=True, null=True)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creditHours = models.FloatField(
        verbose_name='Credit Hours', blank=True, null=True)
    
    midMark = models.FloatField(
        verbose_name='Midterm Mark', blank=True, null=True)
    midAddDate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    midLastEditDate = models.DateTimeField(blank=True, null=True)
    midLock = models.BooleanField(default=False)
    
    finalMark = models.FloatField(
        verbose_name='Final Mark', blank=True, null=True)
    finalAddDate = models.DateTimeField(blank=True, null=True)
    finalLastEditDate = models.DateTimeField(blank=True, null=True)
    finalLock = models.BooleanField(default=True)
    
    gradePoint = models.FloatField(
        verbose_name='Grade Point', blank=True, null=True)
    grade = models.CharField(
        max_length=12, choices=gradeChoice, default='F')
    lastEditDate = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                # conditions=Q(is_active=True),
                fields=['assignCourse', 'student'],
                name="unique_courseResult"
            )
        ]
    
    def __str__(self):
        return f"{self.assignCourse.course} {self.student}"

    def save(self, *args, **kwargs):
        if not self.student in self.assignCourse.student.all():
            raise ValueError("settings.AUTH_USER_MODEL not registered in this course")
        if self.pk: # Update time
            obj = CourseResult.objects.get(pk=self.pk)
            if obj.midLock and obj.midMark != self.midMark:
                raise ValueError("Sorry you can't change Mid term result")
            if obj.finalLock and obj.finalMark != self.finalMark:
                raise ValueError("Sorry you can't change final term result")
            if obj.midMark and self.midMark and obj.midMark != self.midMark:
                self.midLastEditDate = self.lastEditDate
            if not obj.finalMark and self.finalMark:
                self.finalAddDate = self.lastEditDate
                self.finalLastEditDate = self.lastEditDate
            if obj.finalMark and self.finalMark and obj.finalMark != self.finalMark:
                self.finalLastEditDate = self.lastEditDate
            gradeValue = 0
            if self.grade == 'A+':
                gradeValue = 4
            if self.grade == 'A':
                gradeValue = 3.75
            if self.grade == 'A-':
                gradeValue = 3.5
            if self.grade == 'B+':
                gradeValue = 3.25
            if self.grade == 'B':
                gradeValue = 3
            if self.grade == 'B-':
                gradeValue = 2.75
            if self.grade == 'C+':
                gradeValue = 2.5
            if self.grade == 'C':
                gradeValue = 2.25
            if self.grade == 'C-':
                gradeValue = 2
            self.gradePoint = gradeValue * self.creditHours
        else: #creation time
            if self.finalMark:
                raise ValueError("Sorry you can't assign final exam marks before mid terms")
            if not self.midMark:
                raise ValueError("Sorry you have to assign mid term exam marks.")
            if self.midMark:
                self.midLastEditDate = self.lastEditDate
        super(CourseResult, self).save(*args, **kwargs)


class SemResult(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.PROTECT, blank=True, null=True)
    session = models.ForeignKey(Session, on_delete=models.PROTECT, blank=True, null=True)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    totalCredit = models.FloatField(
        verbose_name='Total Credit', blank=True, null=True)
    earnedCredit = models.FloatField(
        verbose_name='Earned Credit', blank=True, null=True)
    sgpa = models.FloatField(verbose_name='SGPA', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    lastEditDate = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                # conditions=Q(is_active=True),
                fields=['semester', 'session', 'student'],
                name="unique_semisterResult"
            )
        ]

    def __str__(self):
        return f"{self.semester} {self.session} {self.student}"
    
    def save(self, *args, **kwargs):
        courseResults = CourseResult.objects.filter(student=self.student, assignCourse__semester=self.semester, assignCourse__session=self.session)
        totalCredit = 0
        earnedCredit = 0
        totallPoint = 0
        if len(courseResults):
            for result in courseResults:
                totalCredit += result.creditHours
                if not result.grade == 'F':
                    earnedCredit += result.creditHours
                totallPoint += result.gradePoint
        self.totalCredit = totalCredit
        self.earnedCredit = earnedCredit
        self.sgpa = totallPoint / totalCredit
        super(SemResult, self).save(*args, **kwargs)

