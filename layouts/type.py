from graphene_django import DjangoObjectType
from .models import Depertment, Semester, Program, Session


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