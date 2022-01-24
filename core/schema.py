import graphene
from django.db import models
from graphene.types import schema
from graphene_django import DjangoObjectType
from .models import User as UserModel
from django.contrib.auth.models import Group
from graphene_django.converter import convert_django_field


@convert_django_field.register(models.PositiveBigIntegerField)
def convert_bigint_to_float(field, registry=None):
    return graphene.Float(description=field.help_text, required=not field.null)


class User(DjangoObjectType):
    class Meta:
        model = UserModel


class Groups(DjangoObjectType):
    class Meta:
        model = Group


class Query(graphene.ObjectType):
    users = graphene.List(User)
    groups = graphene.List(Groups)

    def resolve_users(self, info):
        return UserModel.objects.all()

    def resolve_groups(self, info):
        return Group.objects.all()


schema = graphene.Schema(query=Query)
