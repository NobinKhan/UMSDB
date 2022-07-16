from django.db import models
from django.apps import apps
from django.contrib import auth
from django.utils import timezone
from django.core.mail import send_mail
from django_countries.fields import CountryField
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from layouts.models import Session, Semester, Department, Program
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


def userDirectoryPath(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


# designationChoices = [
#         ('HoD', 'HoD'),
#         ('Co-ordinator', 'Co-ordinator'),
#         ('AssosiateProfessor', 'AssosiateProfessor'),
#         ('AssistantProfessor', 'AssistantProfessor'),
#         ('Professor', 'Professor'),
#         ('Lecturer', 'Lecturer'),
#         ('SeniorLecturer', 'SeniorLecturer'),
#         ('Accountant', 'Accountant'),
#         ('Registrar', 'Registrar'),
#     ]

class Nationality(models.Model):
    name = models.CharField(
        verbose_name='Nationality', max_length=50, blank=True, null=True)

    def __str__(self):
        if not self.name:
            return ''
        return str(self.name)


class Designation(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        if not self.name:
            return ''
        return str(self.name)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given user must have email address')
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name)
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)

    def with_perm(self, perm, is_active=True, include_superusers=True, backend=None, obj=None):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    'You have multiple authentication backends configured and '
                    'therefore must provide the `backend` argument.'
                )
        elif not isinstance(backend, str):
            raise TypeError(
                'backend must be a dotted import path string (got %r).'
                % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, 'with_perm'):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()


class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    username_validator = UnicodeUsernameValidator()
    
    genderChoices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    # Personal Information ######
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
        null=True,
        blank=True
    )

    email = models.EmailField(_('email address'), unique=True)
    date_of_birth = models.DateField(verbose_name=_("Date of birth"))
    gender = models.CharField(
        max_length=20,
        choices=genderChoices,
        default='Male',
    )

    
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    joinedSession = models.ForeignKey(
        Session, on_delete=models.PROTECT, blank=True, null=True)

    # Role Information ######

    # student Information
    isStudent = models.BooleanField(
        default=False, null=True, blank=True
    )
    typeChoices = [
        ('New', 'New'),
        ('TC', 'TC'),
    ]
    studentAddmissionType = models.CharField(
        verbose_name='Addmission Type',
        max_length=5,
        choices=typeChoices,
        null=True,
        blank=True,
    )
    program = models.ForeignKey(
        Program, 
        on_delete=models.PROTECT,
        blank=True, 
        null=True
    )
    joinedSemester = models.ForeignKey(
        Semester, on_delete=models.PROTECT, blank=True, null=True)


    # teacher Information
    isTeacher = models.BooleanField(
        default=False, null=True, blank=True
    )
    department = models.ForeignKey(Department, on_delete=models.PROTECT, blank=True, null=True)
    
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT, null=True, blank=True)

    # Staff information
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can do which operation'),
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['date_of_birth', 'email']

    # class Meta:
    #     verbose_name = _('user')
    #     verbose_name_plural = _('users')
    #     abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def __str__(self):
        return str(self.email)
    
    def save(self, *args, **kwargs):
        # Save the provided password in hashed format
        # user = super(User, self).save(*args, **kwargs)
        # user.set_password()
        if not self.joinedSession and not self.is_superuser:
            raise ValueError("Joined session data not provided")
        if self.isStudent:
            if self.isTeacher or self.is_staff:
                raise ValueError("User can't be both student, teacher or staff")
            self.department = None
            if self.username:
                check = User.objects.get(pk=self.id)
                if check.program != self.program or check.studentAddmissionType != self.studentAddmissionType:
                    self.username = None
            if not self.username:
                yearLastTwoDigit = str(self.joinedSession)[2:]
                semesterNumber = str(self.joinedSemester.num)
                program = ('0' + str(self.program.num)
                        ) if self.program.num < 10 else str(self.program.num)
                type = '1' if self.studentAddmissionType == 'New' else '7'
                obj = User.objects.filter(isStudent=True,username__contains=yearLastTwoDigit+semesterNumber+program+type).last()
                lastSerial = 0 if not obj else int(str(obj.username)[-3:])
                if lastSerial+1 < 10:
                    serial = '00' + str(lastSerial+1)
                elif lastSerial+1 < 100:
                    serial = '0' + str(lastSerial+1)
                else:
                    serial = str(lastSerial+1)

                self.username = int(yearLastTwoDigit + semesterNumber +
                            program + type + serial)
        
        if self.isTeacher:
            if self.isStudent or self.is_staff:
                raise ValueError("User can't be both student, teacher or staff")
            self.joinedSemester = None
            self.program = None
            self.studentAddmissionType = None
            if self.username:
                check = User.objects.get(pk=self.id)
                if check.department != self.department:
                        self.username = None
            if not self.username:
                staffNumber = '11'
                department = ('0' + str(self.department.num)
                            ) if self.department.num < 10 else str(self.department.num)
                obj = User.objects.filter(isTeacher=True, username__contains=staffNumber+department).last()
                lastSerial = 0 if not obj else int(str(obj.username)[-3:])
                if lastSerial+1 < 10:
                    serial = '00' + str(lastSerial+1)
                elif lastSerial+1 < 100:
                    serial = '0' + str(lastSerial+1)
                else:
                    serial = str(lastSerial+1)
                self.username = int(staffNumber + department + serial)
        
        if self.is_staff:
            if self.isStudent or self.isTeacher:
                raise ValueError("User can't be both student, teacher or staff")
            self.joinedSemester = None
            self.program = None
            self.studentAddmissionType = None
            if not self.username:
                staffNumber = '77'
                obj = User.objects.filter(is_staff=True, username__contains=staffNumber).last()
                lastSerial = 0 if not obj else int(str(obj.username)[-4:])
                if lastSerial+1 < 10:
                    serial = '000' + str(lastSerial+1)
                elif lastSerial+1 < 100:
                    serial = '00' + str(lastSerial+1)
                elif lastSerial+1 < 1000:
                    serial = '0' + str(lastSerial+1)
                else:
                    serial = str(lastSerial+1)
                self.username = int(staffNumber + serial)
        super(User, self).save(*args, **kwargs)

        # return user
    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     """Send an email to this user."""
    #     send_mail(subject, message, from_email, [self.email], **kwargs)


class PreviousEducation(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
        # Previous Education (Academic Information)
    # SSC Section
    ssceqChoices = [
        ('SSC', 'SSC'),
        ('O Level', 'O Level'),
        ('IGCSE', 'IGCSE'),
        ('Dakhil (Madrasha Education Board)', 'Dakhil (Madrasha Education Board)'),
        ('Vocational SSC (Technical Education Board)', 'Vocational SSC (Technical Education Board)'),
        ('Other', 'Other'),
    ]
    ssceq = models.CharField(
        verbose_name='SSC or Equivalent',
        max_length=50,
        choices=ssceqChoices,
        default='SSC',
        blank=True, null=True,
    )
    sscGpa = models.FloatField(verbose_name='SSC GPA', blank=True, null=True)
    sscYear = models.SmallIntegerField(
        verbose_name='SSC Year', blank=True, null=True)
    sscFile = models.FileField(
        verbose_name='SSC Certificate/Transcript', upload_to=userDirectoryPath, blank=True, null=True)

    # HSC Section
    hsceqChoices = [
        ('HSC', 'HSC'),
        ('A Level', 'A Level'),
        ('Alim (Madrasha Education Board)', 'Alim (Madrasha Education Board)'),
        ('Vocational HSC (Technical Education Board)', 'Vocational HSC (Technical Education Board)'),
        ('Diploma In Bussiness studies', 'Diploma In Bussiness studies'),
        ('Other', 'Other'),
    ]
    hsceq = models.CharField(
        verbose_name='HSC or Equivalent',
        max_length=50,
        choices=hsceqChoices,
        default='HSC',
        blank=True, null=True,
    )
    hscGpa = models.FloatField(verbose_name='hsc GPA', blank=True, null=True)
    hscYear = models.SmallIntegerField(
        verbose_name='hsc Year', blank=True, null=True)
    hscfile = models.FileField(
        verbose_name='HSC Certificate/Transcript', upload_to=userDirectoryPath, blank=True, null=True)

    # Bachelor Section
    bachelor = models.CharField(
        verbose_name='Bachelor', max_length=150, blank=True, null=True)
    bscInstitute = models.CharField(
        verbose_name='Institute/University', max_length=150, blank=True, null=True)
    bachelorGpa = models.FloatField(
        verbose_name='GPA/Result', blank=True, null=True)
    bachelorYear = models.SmallIntegerField(
        verbose_name='Passing Year', blank=True, null=True)
    bachelorFile = models.FileField(
        verbose_name='Certificate/Transcript', upload_to=userDirectoryPath, blank=True, null=True)

    # Master Section
    master = models.CharField(
        verbose_name='Master', max_length=150, blank=True, null=True)
    mscInstitute = models.CharField(
        verbose_name='Institute/University', max_length=150, blank=True, null=True)
    masterGpa = models.FloatField(
        verbose_name='GPA/Result', blank=True, null=True)
    masterYear = models.SmallIntegerField(
        verbose_name='Passing Year', blank=True, null=True)
    masterFile = models.FileField(
        verbose_name='Certificate/Transcript', upload_to=userDirectoryPath, blank=True, null=True)

    # Phd Degree Section
    phd = models.CharField(
        verbose_name='Phd Degree', max_length=150, blank=True, null=True)
    phdInstitute = models.CharField(
        verbose_name='Institute/University', max_length=150, blank=True, null=True)
    phdGpa = models.FloatField(
        verbose_name='GPA/Result', blank=True, null=True)
    phdYear = models.SmallIntegerField(
        verbose_name='Passing Year', blank=True, null=True)
    phdFile = models.FileField(
        verbose_name='Certificate/Transcript', upload_to=userDirectoryPath, blank=True, null=True)

    def __str__(self):
        if not self.user:
            return ''
        return self.user.__str__() 


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    permanentAddress = models.CharField(verbose_name=_(
        "Parmanent Address"), max_length=1024, null=True)
    presentAddress = models.CharField(verbose_name=_(
        "Present Address"), max_length=1024, null=True)
    # zip_code = models.CharField(verbose_name=_("Postal Code"), max_length=12)
    # city = models.CharField(verbose_name=_("City"), max_length=1024)
    # country = CountryField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r"^\+(?:[0-9]●?){6,14}[0-9]$", message=_(
        "Enter a valid international mobile phone number starting with +(country code)"))
    mobilePhone = models.CharField(validators=[phone_regex], verbose_name=_(
        "Primary Phone"), max_length=17, blank=True, null=True)
    mobilePhone2 = models.CharField(validators=[phone_regex], verbose_name=_(
        "Secondary phone"), max_length=17, blank=True, null=True)
    nid = models.PositiveBigIntegerField(unique=True, null=True, blank=True)
    birthCertNumber = models.PositiveBigIntegerField(unique=True, null=True)
    nationality = models.ForeignKey(Nationality, blank=True, null=True,on_delete=models.PROTECT)
    fatherName = models.CharField(_('Father Name'), max_length=150, blank=True)
    motherName = models.CharField(_('Mother Name'), max_length=150, blank=True)
    photo = models.ImageField(verbose_name=_(
        "Photo"), upload_to='photos/', default='photos/default-user-avatar.png')

    def __str__(self):
        if not self.user:
            return ''
        return self.user.__str__() 



