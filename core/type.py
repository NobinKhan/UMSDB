from django.contrib.auth.models import Group
from graphene import Field
from graphene_django import DjangoObjectType
from functions.converter import BigInt
from .models import User, Nationality


class UserType(DjangoObjectType):
    nid = Field(BigInt)
    birthCertNumber = Field(BigInt)

    class Meta:
        model = User


class GroupType(DjangoObjectType):
    class Meta:
        model = Group



class NationalityType(DjangoObjectType):

    class Meta:
        model = Nationality