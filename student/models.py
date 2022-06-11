from django.db import models
from core.models import User
from layouts.models import Program, Session, Semester


# Create your models here.


def userDirectoryPath(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    localGuardian = models.CharField(
        verbose_name='Local Guardian', max_length=150, blank=True)
    address = models.CharField(
        verbose_name='Address', max_length=150, blank=True)
    mobilePhone = models.PositiveBigIntegerField(verbose_name=(
        "Mobile Phone"), blank=True, null=True)

    # Previous Education (Academic Information)
    # SSC Section
    ssceqChoices = [
        ('ssc', 'SSC'),
        ('olevel', 'O Level'),
        ('igcse', 'IGCSE'),
        ('dakhil', 'Dakhil (Madrasha Education Board)'),
        ('vssc', 'Vocational SSC (Technical Education Board)'),
        ('other', 'Other'),
    ]
    ssceq = models.CharField(
        verbose_name='SSC or Equivalent',
        max_length=250,
        choices=ssceqChoices,
        default='ssc',
    )
    sscGpa = models.FloatField(verbose_name='SSC GPA', blank=True, null=True)
    sscYear = models.SmallIntegerField(
        verbose_name='SSC Year', blank=True, null=True)
    sscFile = models.FileField(
        verbose_name='SSC Certificate/Transcript', upload_to=userDirectoryPath, blank=True, null=True)

    # HSC Section
    hsceqChoices = [
        ('hsc', 'HSC'),
        ('alevel', 'A Level'),
        ('alim', 'Alim (Madrasha Education Board)'),
        ('vhsc', 'Vocational HSC (Technical Education Board)'),
        ('dbs', 'Diploma In Bussiness studies'),
        ('other', 'Other'),
    ]
    hsceq = models.CharField(
        verbose_name='HSC or Equivalent',
        max_length=250,
        choices=hsceqChoices,
        default='hsc',
    )
    hscGpa = models.FloatField(verbose_name='hsc GPA', blank=True, null=True)
    hscYear = models.SmallIntegerField(
        verbose_name='hsc Year', blank=True, null=True)
    hscfile = models.FileField(
        verbose_name='HSC Certificate/Transcript', upload_to=userDirectoryPath, blank=True, null=True)

    # Bachelor Section
    bachelor = models.CharField(
        verbose_name='Bachelor', max_length=150, blank=True)
    institute = models.CharField(
        verbose_name='Institute/University', max_length=150, blank=True)
    bachelorGpa = models.FloatField(
        verbose_name='GPA/Result', blank=True, null=True)
    bachelorYear = models.SmallIntegerField(
        verbose_name='Passing Year', blank=True, null=True)
    bachelorFile = models.FileField(
        verbose_name='Certificate/Transcript', upload_to=userDirectoryPath, blank=True, null=True)

    # Academic Section
    typeChoices = [
        ('new', 'New'),
        ('tc', 'Transfering Here'),
    ]
    type = models.CharField(
        verbose_name='Addmission Type',
        max_length=250,
        choices=typeChoices,
        default='new',
    )
    program = models.ForeignKey(Program, on_delete=models.PROTECT)
    joinedSemester = models.ForeignKey(
        Semester, on_delete=models.PROTECT, blank=True, null=True)
    joinedSession = models.ForeignKey(
        Session, on_delete=models.PROTECT, blank=True, null=True)

    # Student ID
    uid = models.SmallIntegerField(
        verbose_name='Student ID', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.uid:
            yearLastTwoDigit = str(self.joinedSession)[2:]
            semesterNumber = str(self.joinedSemester.num)
            program = ('0' + str(self.program.num)
                       ) if self.program.num < 10 else str(self.program.num)
            type = '1' if self.type == 'new' else '7'
            obj = Student.objects.filter(
                uid__contains=yearLastTwoDigit+semesterNumber+program+type).last()
            lastSerial = 0 if not obj else int(str(obj.uid)[-3:])
            if lastSerial+1 < 10:
                serial = '00' + str(lastSerial+1)
            elif lastSerial+1 < 100:
                serial = '0' + str(lastSerial+1)
            else:
                serial = str(lastSerial+1)

            self.uid = int(yearLastTwoDigit + semesterNumber +
                           program + type + serial)

            # raise ValueError("Uid field is empty")
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.uid)
