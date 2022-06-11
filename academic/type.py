from .models import AssignCourse, CourseName, Course
from graphene_django import DjangoObjectType







class AssignCourseType(DjangoObjectType):
    class Meta:
        model = AssignCourse



class CourseNameType(DjangoObjectType):
    class Meta:
        model = CourseName


class CourseType(DjangoObjectType):
    class Meta:
        model = Course