from django.contrib.auth.models import Group
from graphene import Field
from graphene_django import DjangoObjectType
from functions.converter import BigInt
from .models import User, Nationality, Designation, PreviousEducation, Profile


class UserType(DjangoObjectType):
    class Meta:
        model = User


class GroupType(DjangoObjectType):
    class Meta:
        model = Group


class NationalityType(DjangoObjectType):
    class Meta:
        model = Nationality


class DesignationType(DjangoObjectType):
    class Meta:
        model = Designation


class PreviousEducationType(DjangoObjectType):
    class Meta:
        model = PreviousEducation


class ProfileType(DjangoObjectType):
    nid = Field(BigInt)
    birthCertNumber = Field(BigInt)
    class Meta:
        model = Profile