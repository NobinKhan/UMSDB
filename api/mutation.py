import graphene
from academic.schema import CreateSession, UpdateSession, DeleteSession

class Mutation(graphene.ObjectType):
    createSession = CreateSession.Field()
    updateSession = UpdateSession.Field()
    deleteSession = DeleteSession.Field()