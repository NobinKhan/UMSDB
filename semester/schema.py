from graphene_django import DjangoObjectType
from .models import AssignCourse


class AssignCourseType(DjangoObjectType):
    class Meta:
        model = AssignCourse
