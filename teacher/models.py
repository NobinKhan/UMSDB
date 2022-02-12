from django.db import models
from core.models import User
from academic.models import Depertment, Program, Semester, Session

# Create your models here.


def userDirectoryPath(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
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

    # Master Section
    master = models.CharField(
        verbose_name='Master', max_length=150, blank=True)
    institute = models.CharField(
        verbose_name='Institute/University', max_length=150, blank=True)
    masterGpa = models.FloatField(
        verbose_name='GPA/Result', blank=True, null=True)
    masterYear = models.SmallIntegerField(
        verbose_name='Passing Year', blank=True, null=True)
    masterFile = models.FileField(
        verbose_name='Certificate/Transcript', upload_to=userDirectoryPath, blank=True, null=True)

    # Phd Degree Section
    phd = models.CharField(
        verbose_name='Phd Degree', max_length=150, blank=True)
    institute = models.CharField(
        verbose_name='Institute/University', max_length=150, blank=True)
    phdGpa = models.FloatField(
        verbose_name='GPA/Result', blank=True, null=True)
    phdYear = models.SmallIntegerField(
        verbose_name='Passing Year', blank=True, null=True)
    phdFile = models.FileField(
        verbose_name='Certificate/Transcript', upload_to=userDirectoryPath, blank=True, null=True)

    # Academic Section
    depertment = models.ForeignKey(Depertment, on_delete=models.PROTECT)
    joinedYear = models.ForeignKey(
        Session, on_delete=models.PROTECT, blank=True, null=True)
    roleChoices = [
        ('Department Head', 'Department Head'),
        ('Co-ordinator', 'Co-ordinator'),
        ('Assosiate Professor', 'Assosiate Professor'),
        ('Assistant Professor', 'Assistant Professor'),
        ('Professor', 'Professor'),
        ('Lecturer', 'Lecturer'),
        ('Senior Lecturer', 'Senior Lecturer'),
    ]
    role = models.CharField(
        verbose_name='Role',
        max_length=250,
        choices=roleChoices,
        default='Lecturer',
    )

    # Teacher ID
    uid = models.SmallIntegerField(
        verbose_name='Teacher ID', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.uid:
            staffNumber = '11'
            depertment = ('0' + str(self.depertment.num)
                          ) if self.depertment.num < 10 else str(self.depertment.num)
            obj = Teacher.objects.filter(
                uid__contains=staffNumber+depertment).last()
            lastSerial = 0 if not obj else int(str(obj.uid)[-3:])
            if lastSerial+1 < 10:
                serial = '00' + str(lastSerial+1)
            elif lastSerial+1 < 100:
                serial = '0' + str(lastSerial+1)
            else:
                serial = str(lastSerial+1)

            self.uid = int(staffNumber + depertment + serial)

            # raise ValueError("Uid field is empty")
        super(Teacher, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.uid)
