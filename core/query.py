from graphene import ObjectType, List, Int, String, Float
from .type import UserType, GroupType, NationalityType
from .models import User, Nationality
from django.contrib.auth.models import Group
from django.db import models
# from graphene_django.converter import convert_django_field

# @convert_django_field.register(models.PositiveBigIntegerField)
# def convert_bigint_to_float(field, registry=None):
#     print("i am called from core")
#     return Float(description=field.help_text, required=not field.null)


class Query(ObjectType):
    users = List(UserType, id=Int(), email = String())
    groups = List(GroupType, id=Int())
    nationalities = List(NationalityType, id=Int())

    def resolve_users(self, info, id=None, email=None):
        if id:
            return User.objects.filter(pk=id)
        if email:
            return User.objects.filter(email=email)
        return User.objects.all()

    def resolve_groups(self, info, id=None):
        if id:
            return Group.objects.filter(pk=id)
        return Group.objects.all()
    
    def resolve_nationalities(self, info, id=None):
        if id:
            return Nationality.objects.filter(pk=id)
        return Nationality.objects.all()