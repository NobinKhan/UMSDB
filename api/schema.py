import graphene
from .query import Query
from .mutation import Mutation

# from graphene.types import schema







schema = graphene.Schema(query=Query, mutation=Mutation)
