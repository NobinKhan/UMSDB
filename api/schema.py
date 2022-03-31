import graphene
from .query import Query

# from graphene.types import schema







schema = graphene.Schema(query=Query)
