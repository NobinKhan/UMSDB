import graphene
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


class CreateSession(graphene.Mutation):
    session = graphene.Field(SessionType)
    class Arguments:
        year = graphene.Int(required=True)
    def mutate(self, info, year):
        session = Session(year=year)
        session.save()
        return CreateSession(session=session)


class UpdateSession(graphene.Mutation):
    session = graphene.Field(SessionType)
    class Arguments:
        id = graphene.Int(required=True)
        year = graphene.Int(required=True)
    def mutate(self, info, year, id):
        session = Session.objects.get(id=id)
        session.year = year
        session.save()
        return UpdateSession(session=session)


class DeleteSession(graphene.Mutation):
    message = graphene.String()
    class Arguments:
        id = graphene.Int(required=True)
    def mutate(self, info, id):
        session = Session.objects.get(id=id)
        session.delete()
        return DeleteSession(message=f"Data of id {id} Succesfully deleted")


class CourseNameType(DjangoObjectType):
    class Meta:
        model = CourseName


class CourseType(DjangoObjectType):
    class Meta:
        model = Course