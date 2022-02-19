from .models import User
from django.contrib.auth.models import Group
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = User


class GroupType(DjangoObjectType):
    class Meta:
        model = Group


