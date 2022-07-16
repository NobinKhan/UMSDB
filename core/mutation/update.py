from django.contrib.auth.models import Group
from functions.handle_error import get_object_or_None
from layouts.models import Semester, Session, Program, Department
from core.models import User, Nationality, Designation, Profile, PreviousEducation
from graphene import InputObjectType, String, Mutation, Field, Date, Int, Float, ID
from core.type import UserType, GroupType, NationalityType, ProfileType, DesignationType, PreviousEducationType


class UpdateNationality(Mutation):
    class Arguments:
        id = ID(required=True)
        name = String(required=True)
    nationality = Field(NationalityType)
    def mutate(root, info, name, id):
        oldNationality = get_object_or_None(Nationality, pk=id)
        if oldNationality:
            oldNationality.name = name
            oldNationality.save()
            return UpdateNationality(nationality=oldNationality)
        return None


class UpdateDesignation(Mutation):
    class Arguments:
        id = ID(required=True)
        name = String(required=True)
    designation = Field(DesignationType)
    def mutate(root, info, name, id):
        oldDesignation = get_object_or_None(Designation, pk=id)
        if oldDesignation:
            oldDesignation.name = name
            oldDesignation.save()
            return UpdateDesignation(designation=oldDesignation)
        return None


class UpdateProfileInput(InputObjectType):
    id = ID(required=True)
    firstName = String()
    lastName = String()
    permanentAddress = String()
    presentAddress = String()
    mobilePhone = String()
    mobilePhone2 = String()
    nid = Float()
    birthCertNumber = Float()
    nationality = ID()
    fatherName = String()
    motherName = String()
    photo = String()


class UpdateProfile(Mutation):
    class Arguments:
        data = UpdateProfileInput()
    profile = Field(ProfileType)
    def mutate(root, info, data=None):
        nationalityInstance = get_object_or_None(Nationality, pk=data.nationality)
        oldProfile = get_object_or_None(Profile, pk=data.id)
        if oldProfile:
            if data.firstName:
                oldProfile.first_name = data.firstName
            if data.lastName:
                oldProfile.last_name = data.lastName
            if data.permanentAddress:
                oldProfile.permanentAddress = data.permanentAddress
            if data.presentAddress:
                oldProfile.presentAddress = data.presentAddress
            if data.mobilePhone:
                Profile.phone_regex(data.mobilePhone)
                oldProfile.mobilePhone = data.mobilePhone
            if data.mobilePhone2:
                Profile.phone_regex(data.mobilePhone2)
                oldProfile.mobilePhone2 = data.mobilePhone2
            if data.nid:
                oldProfile.nid = data.nid
            if data.birthCertNumber:
                oldProfile.birthCertNumber = data.birthCertNumber
            if nationalityInstance:
                oldProfile.nationality = nationalityInstance
            if data.fatherName:
                oldProfile.fatherName = data.fatherName
            if data.motherName:
                oldProfile.motherName = data.motherName
            if data.photo:
                oldProfile.photo = data.photo
            return UpdateProfile(profile=oldProfile)

