from graphene_django import DjangoObjectType
from .models import Teacher


class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher
