import graphene
from semester.models import AssignCourse
from .models import User
from django.db import models
from teacher.models import Teacher
from student.models import Student
from django.contrib.auth.models import Group
from graphene_django import DjangoObjectType
from graphene_django.converter import convert_django_field
# from graphene.types import schema


@convert_django_field.register(models.PositiveBigIntegerField)
def convert_bigint_to_float(field, registry=None):
    return graphene.Float(description=field.help_text, required=not field.null)


class AssignCourseType(DjangoObjectType):
    class Meta:
        model = AssignCourse


class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher


class StudentTypes(DjangoObjectType):
    class Meta:
        model = Student


class UserType(DjangoObjectType):
    class Meta:
        model = User


class GroupType(DjangoObjectType):
    class Meta:
        model = Group


class Query(graphene.ObjectType):
    assignCourse = graphene.List(AssignCourseType)
    teachers = graphene.List(TeacherType)
    students = graphene.List(StudentTypes)
    users = graphene.List(UserType)
    groups = graphene.List(GroupType)

    def resolve_assignCourse(self, info):
        return AssignCourse.objects.all()

    def resolve_teachers(self, info):
        return Teacher.objects.all()

    def resolve_students(self, info):
        return Student.objects.all()

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_groups(self, info):
        return Group.objects.all()


schema = graphene.Schema(query=Query)
