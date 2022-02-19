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
# from graphene.types import schema


@convert_django_field.register(models.PositiveBigIntegerField)
def convert_bigint_to_float(field, registry=None):
    return graphene.Float(description=field.help_text, required=not field.null)


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
