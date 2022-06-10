import graphene
from academic.mutation import CreateSession, UpdateSession, DeleteSession, CreateDepertment, UpdateDepertment, DeleteDepartment

class Mutation(graphene.ObjectType):
    createDepartment = CreateDepertment.Field()
    updateDepertment = UpdateDepertment.Field()
    deleteDepartment = DeleteDepartment.Field()
    createSession = CreateSession.Field()
    updateSession = UpdateSession.Field()
    deleteSession = DeleteSession.Field()