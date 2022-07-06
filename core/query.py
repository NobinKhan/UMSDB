from django.contrib.auth.models import Group
from graphene_django import DjangoObjectType
from graphene import ObjectType, List, Int, String, Float, Field, NonNull, ID, Boolean
from .models import User, Nationality, Designation, PreviousEducation, Profile
from .type import UserType, GroupType, NationalityType, DesignationType, PreviousEducationType, ProfileType
# from graphene_django.converter import convert_django_field

# @convert_django_field.register(models.PositiveBigIntegerField)
# def convert_bigint_to_float(field, registry=None):
#     print("i am called from core")
#     return Float(description=field.help_text, required=not field.null)


class Query(ObjectType):
    users = List(UserType, designation=ID())
    students = List(UserType)
    teachers = List(UserType)
    staffs = List(UserType)
    user = Field(UserType, id=Int(), username = String())
    groups = List(GroupType, id=Int())
    nationalities = List(NationalityType, id=Int())
    designations = List(DesignationType, id=Int())
    previousEducations = List(PreviousEducationType, id=Int())
    profiles = List(ProfileType, id=Int())

    def resolve_users(self, info, designation=None):
        if designation:
            return User.objects.filter(designation=designation)
        return User.objects.all()
    
    def resolve_students(self, info):
        return User.objects.filter(isStudent=True)
    
    def resolve_teachers(self, info):
        return User.objects.filter(isTeacher=True)
    
    def resolve_staffs(self, info):
        return User.objects.filter(is_staff=True)
    
    def resolve_user(self, info, id=None, username=None):
        if id:
            return User.objects.get(pk=id)
        if username:
            return User.objects.get(username=username)
        return None

    def resolve_groups(self, info, id=None):
        if id:
            return Group.objects.filter(pk=id)
        return Group.objects.all()
    
    def resolve_nationalities(self, info, id=None):
        if id:
            return Nationality.objects.filter(pk=id)
        return Nationality.objects.all()
    
    def resolve_designations(self, info, id=None):
        if id:
            return Designation.objects.filter(pk=id)
        return Designation.objects.all()
    
    def resolve_previousEducations(self, info, id=None):
        if id:
            return PreviousEducation.objects.filter(pk=id)
        return PreviousEducation.objects.all()
    
    def resolve_profiles(self, info, id=None):
        if id:
            return Profile.objects.filter(pk=id)
        return Profile.objects.all()