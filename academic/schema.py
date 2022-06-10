from .models import Depertment, Semester, Program, Session, CourseName, Course
from graphene_django import DjangoObjectType


class DepertmentType(DjangoObjectType):
    class Meta:
        model = Depertment


class SemesterType(DjangoObjectType):
    class Meta:
        model = Semester


class ProgramType(DjangoObjectType):
    class Meta:
        model = Program


class SessionType(DjangoObjectType):
    class Meta:
        model = Session


class CourseNameType(DjangoObjectType):
    class Meta:
        model = CourseName


class CourseType(DjangoObjectType):
    class Meta:
        model = Course