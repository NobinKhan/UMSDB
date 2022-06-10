from graphene import Schema, ObjectType, Float
from django.db import models
from core.query import Query as crqr
from core.mutation import Mutation as crmt
# from graphene_django.converter import convert_django_field
# from .query import Query
# from .mutation import Mutation

# from graphene.types import schema
# @convert_django_field.register(models.PositiveBigIntegerField)
# def convert_bigint_to_float(field, registry=None):
#     return Float(description=field.help_text, required=not field.null)

class Query(crqr, ObjectType):
    pass


class Mutation(crmt, ObjectType):
    pass





schema = Schema(query=Query, mutation=Mutation)
