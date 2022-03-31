import graphene
from django.db import models
from graphene_django.converter import convert_django_field
from core.models import User
from core.schema import GroupType, UserType
from django.contrib.auth.models import Group
from semester.models import AssignCourse

from semester.schema import AssignCourseType
from student.models import Student
from student.schema import StudentTypes
from teacher.models import Teacher
from teacher.schema import TeacherType
from academic.schema import DepertmentType, SemesterType, SessionType, ProgramType, CourseNameType, CourseType
from academic.models import Depertment, Semester, Program, Session, CourseName, Course




@convert_django_field.register(models.PositiveBigIntegerField)
def convert_bigint_to_float(field, registry=None):
    return graphene.Float(description=field.help_text, required=not field.null)


class Query(graphene.ObjectType):
    users = graphene.List(UserType, id=graphene.Int())
    groups = graphene.List(GroupType, id=graphene.Int())
    students = graphene.List(StudentTypes, id=graphene.Int())
    teachers = graphene.List(TeacherType, id=graphene.Int())
    depertment = graphene.List(DepertmentType, id=graphene.Int())
    semester = graphene.List(SemesterType, id=graphene.Int())
    program = graphene.List(ProgramType, id=graphene.Int())
    session = graphene.List(SessionType, id=graphene.Int())
    courseName = graphene.List(CourseNameType, id=graphene.Int())
    course = graphene.List(CourseType, id=graphene.Int())
    assignCourse = graphene.List(AssignCourseType, id=graphene.Int())

    def resolve_users(self, info, id=None):
        if id:
            return User.objects.filter(pk=id)
        return User.objects.all()

    def resolve_groups(self, info, id=None):
        if id:
            return Group.objects.filter(pk=id)
        return Group.objects.all()

    def resolve_students(self, info, id=None):
        if id:
            return Student.objects.filter(pk=id)
        return Student.objects.all()

    def resolve_teachers(self, info, id=None):
        if id:
            return Teacher.objects.filter(pk=id)
        return Teacher.objects.all()

    def resolve_depertment(self, info, id=None):
        if id:
            return Depertment.objects.filter(pk=id)
        return Depertment.objects.all()

    def resolve_semester(self, info, id=None):
        if id:
            return Semester.objects.filter(pk=id)
        return Semester.objects.all()

    def resolve_program(self, info, id=None):
        if id:
            return Program.objects.filter(pk=id)
        return Program.objects.all()

    def resolve_session(self, info, id=None):
        if id:
            return Session.objects.filter(pk=id)
        return Session.objects.all()

    def resolve_courseName(self, info, id=None):
        if id:
            return CourseName.objects.filter(pk=id)
        return CourseName.objects.all()

    def resolve_course(self, info, id=None):
        if id:
            return Course.objects.filter(pk=id)
        return Course.objects.all()

    def resolve_assignCourse(self, info, id=None):
        if id:
            return AssignCourse.objects.filter(pk=id)
        return AssignCourse.objects.all()
