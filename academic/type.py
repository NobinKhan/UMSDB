from .models import AssignCourse, Course, Period, Shedule, Attendance, CourseResult, SemResult, AttendanceStatus, CourseStatus
from graphene_django import DjangoObjectType




class CourseType(DjangoObjectType):
    class Meta:
        model = Course


class PeriodType(DjangoObjectType):
    class Meta:
        model = Period


class SheduleType(DjangoObjectType):
    class Meta:
        model = Shedule


class AssignCourseType(DjangoObjectType):
    class Meta:
        model = AssignCourse


class CourseStatusType(DjangoObjectType):
    class Meta:
        model = CourseStatus


class AttendanceType(DjangoObjectType):
    class Meta:
        model = Attendance


class AttendanceStatusType(DjangoObjectType):
    class Meta:
        model = AttendanceStatus


class CourseResultType(DjangoObjectType):
    class Meta:
        model = CourseResult


class SemResultType(DjangoObjectType):
    class Meta:
        model = SemResult