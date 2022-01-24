import graphene
from graphene.types import schema
from graphene_django import DjangoObjectType
from .models import User as UserModel
from django.contrib.auth.models import Group


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
