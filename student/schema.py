from graphene_django import DjangoObjectType
from .models import Student


class StudentTypes(DjangoObjectType):
    class Meta:
        model = Student
