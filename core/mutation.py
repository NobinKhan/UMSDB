from django.contrib.auth.models import Group
from graphene import InputObjectType, String, Mutation, Field, Date, Int, ObjectType, Float, ID
from functions.handle_error import get_object_or_None
from .type import UserType, GroupType, NationalityType
from .models import User, Nationality
# import graphql_jwt




class CreateNationality(Mutation):
    class Arguments:
        name = String(required=True)
    nationality = Field(NationalityType)
    def mutate(root, info, name):
        newNationality = Nationality(name = name)
        newNationality.save()
        return CreateNationality(nationality=newNationality)



class CreateGroup(Mutation):
    class Arguments:
        name = String(required=True)
    group = Field(GroupType)
    def mutate(root, info, name):
        newGroup = Group(name = name)
        newGroup.save()
        return CreateGroup(group=newGroup)



class UserInput(InputObjectType):
    userName = String(required=True)
    firstName = String(required=True)
    lastName = String(required=True)
    email = String(required=True)
    dateOfBirth = Date(required=True)
    gender = String(required=True)
    permanentAddress = String(required=True)
    presentAddress = String(required=True)
    mobilePhone = String(required=True)
    mobilePhone2 = String()
    nid = Float()
    birthCertNumber = Float(required=True)
    nationality = ID(required=True)
    fatherName = String(required=True)
    motherName = String(required=True)
    photo = String(required=True)
    password = String(required=True)
    group = String(required=True)


class CreateUser(Mutation):
    class Arguments:
        data = UserInput()
    user = Field(UserType)
    def mutate(root, info, data=None):
        nationalityInstance = get_object_or_None(Nationality, pk=data.nationality)
        newUser = User(
            username = data.userName,
            first_name = data.firstName,
            last_name = data.lastName,
            email = data.email,
            date_of_birth = data.dateOfBirth,
            gender = data.gender,
            permanentAddress = data.permanentAddress,
            presentAddress = data.presentAddress,
            mobilePhone = data.mobilePhone,
            mobilePhone2 = data.mobilePhone2,
            nid = data.nid,
            birthCertNumber = data.birthCertNumber,
            nationality = nationalityInstance,
            fatherName = data.fatherName,
            motherName = data.motherName,
            photo = data.photo,
        )
        newUser.set_password(data.password)
        newUser.save()
        userGroup = get_object_or_None(Group, name=data.group)
        if userGroup:
            newUser.groups.add(userGroup)

        return CreateUser(user=newUser)



class Mutation(ObjectType):
#   token_auth = graphql_jwt.ObtainJSONWebToken.Field()
#   verify_token = graphql_jwt.Verify.Field()
#   refresh_token = graphql_jwt.Refresh.Field()
  createNationality = CreateNationality.Field()
  createGroup = CreateGroup.Field()
  createUser = CreateUser.Field()