from django.db import models
from core.models import User

# Create your models here.
def userDirectoryPath(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Student(models.Models):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    localGuardian = models.CharField(verbose_name='Local Guardian', max_length=150, blank=True)
    address = models.CharField(verbose_name='Address', max_length=150, blank=True)
    mobilePhone = models.PositiveBigIntegerField(verbose_name=("Mobile Phone"), max_length=17, blank=True, null=True)

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
        max_length=2,
        choices=ssceqChoices,
        default='ssc',
    )
    sscGpa = models.FloatField(verbose_name='SSC GPA', blank=True, null=True)
    sscYear = models.SmallIntegerField(verbose_name='SSC Year', blank=True, null=True)
    sscFile = models.FileField(verbose_name='SSC Certificate/Transcript',upload_to = userDirectoryPath)

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
        max_length=2,
        choices=hsceqChoices,
        default='hsc',
    )
    hscGpa = models.FloatField(verbose_name='hsc GPA', blank=True, null=True)
    hscYear = models.SmallIntegerField(verbose_name='hsc Year', blank=True, null=True)
    hscfile = models.FileField(verbose_name='HSC Certificate/Transcript', upload_to = userDirectoryPath)

    # Bachelor Section
    bachelor = models.CharField(verbose_name='Bachelor', max_length=150, blank=True)
    institute = models.CharField(verbose_name='Institute/University', max_length=150, blank=True)
    bachelorGpa = models.FloatField(verbose_name='GPA/Result', blank=True, null=True)
    bachelorYear = models.SmallIntegerField(verbose_name='Passing Year', blank=True, null=True)
    bachelorFile = models.FileField(verbose_name='Certificate/Transcript', upload_to = userDirectoryPath)

    # Academic Section
    
    # Student ID
