import graphene
from functions.handle_error import get_object_or_None
from .models import Depertment, Semester, Program, Session, CourseName, Course
from .schema import SessionType, DepertmentType


class CreateDepertment(graphene.Mutation):
    department = graphene.Field(DepertmentType)
    class Arguments:
        name = graphene.String(required=True)
        num = graphene.Int(required=True)
    def mutate(self, info, name, num):
        department = Depertment(name=name, num=num)
        department.save()
        return CreateDepertment(department=department)


class UpdateDepertment(graphene.Mutation):
    department = graphene.Field(DepertmentType)
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        num = graphene.Int()
    def mutate(self, info, id, name=None, num=None):
        department = get_object_or_None(Depertment, id=id)
        if department:
            if name:
                department.name = name
            if num:
                department.num = num
            department.save()
        return UpdateDepertment(department=department)


class DeleteDepartment(graphene.Mutation):
    message = graphene.String()
    class Arguments:
        id = graphene.Int(required=True)
    def mutate(self, info, id):
        department = get_object_or_None(Depertment,id=id)
        if department:
            department.delete()
            return DeleteDepartment(message=f"Data of id {id} Succesfully deleted")
        return DeleteDepartment(message=None)


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
        session = get_object_or_None(Session, id=id)
        if session:
            session.year = year
            session.save()
        return UpdateSession(session=session)


class DeleteSession(graphene.Mutation):
    message = graphene.String()
    class Arguments:
        id = graphene.Int(required=True)
    def mutate(self, info, id):
        session = get_object_or_None(Session,id=id)
        if session:
            session.delete()
            return DeleteSession(message=f"Data of id {id} Succesfully deleted")
        return DeleteSession(message=None)
