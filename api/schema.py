from graphene import Schema, ObjectType, Float
from django.db import models
from core.query import Query as crqr
from core.mutation.mutation import Mutation as crmt
from academic.query import Query as acqr
from academic.mutation.mutation import Mutation as acmt


class Query(crqr, acqr, ObjectType):
    pass


class Mutation(crmt, acmt, ObjectType):
    pass





schema = Schema(query=Query, mutation=Mutation)
