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


class UpdateNationality(Mutation):
    class Arguments:
        id = ID(required=True)
        name = String(required=True)
    nationality = Field(NationalityType)
    message = String()
    def mutate(root, info, name, id):
        oldNationality = get_object_or_None(Nationality, pk=id)
        if oldNationality:
            oldNationality.name = name
            oldNationality.save()
            return UpdateNationality(nationality=oldNationality)
        return UpdateNationality(message="Failed - Object Not found")


class DeleteNationality(Mutation):
    class Arguments:
        id = ID(required=True)
    message = String()
    def mutate(root, info, id):
        oldNationality = get_object_or_None(Nationality, pk=id)
        if oldNationality:
            oldNationality.delete()
            return DeleteNationality(message="Succes")
        return DeleteNationality(message="Failed - Object Not found")



class CreateGroup(Mutation):
    class Arguments:
        name = String(required=True)
    group = Field(GroupType)
    def mutate(root, info, name):
        newGroup = Group(name = name)
        newGroup.save()
        return CreateGroup(group=newGroup)


class UpdateGroup(Mutation):
    class Arguments:
        id = ID(required=True)
        name = String(required=True)
    group = Field(GroupType)
    message = String()
    def mutate(root, info, name, id):
        oldGroup = get_object_or_None(Group, pk=id)
        if oldGroup:
            oldGroup.name = name
            oldGroup.save()
            return UpdateGroup(group=oldGroup)
        return UpdateGroup(message="Failed - Object Not found")



class DeleteGroup(Mutation):
    class Arguments:
        id = ID(required=True)
    message = String()
    def mutate(root, info, id):
        oldGroup = get_object_or_None(Group, pk=id)
        if oldGroup:
            oldGroup.delete()
            return DeleteGroup(message="Succes")
        return DeleteGroup(message="Failed - Object Not found")


class CreateUserInput(InputObjectType):
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
        data = CreateUserInput()
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


class UpdateUserInput(InputObjectType):
    id = ID(required=True)
    userName = String()
    firstName = String()
    lastName = String()
    email = String()
    dateOfBirth = Date()
    gender = String()
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
    password = String()
    group = String()


class UpdateUser(Mutation):
    class Arguments:
        data = UpdateUserInput()
    user = Field(UserType)
    message = String()
    def mutate(root, info, data=None):
        nationalityInstance = get_object_or_None(Nationality, pk=data.nationality)
        oldUser = get_object_or_None(User, pk=data.id)
        if oldUser:
            if data.userName:
                oldUser.username = data.userName
            if data.firstName:
                oldUser.first_name = data.firstName
            if data.lastName:
                oldUser.last_name = data.lastName
            if data.email:
                oldUser.email = data.email
            if data.dateOfBirth:
                oldUser.date_of_birth = data.dateOfBirth
            if data.gender:
                oldUser.gender = data.gender
            if data.permanentAddress:
                oldUser.permanentAddress = data.permanentAddress
            if data.presentAddress:
                oldUser.presentAddress = data.presentAddress
            if data.mobilePhone:
                oldUser.mobilePhone = data.mobilePhone
            if data.mobilePhone2:
                oldUser.mobilePhone2 = data.mobilePhone2
            if data.nid:
                oldUser.nid = data.nid
            if data.birthCertNumber:
                oldUser.birthCertNumber = data.birthCertNumber
            if nationalityInstance:
                oldUser.nationality = nationalityInstance
            if data.fatherName:
                oldUser.fatherName = data.fatherName
            if data.motherName:
                oldUser.motherName = data.motherName
            if data.photo:
                oldUser.photo = data.photo
            if data.password:
                oldUser.set_password(data.password)
            oldUser.save()
            userGroup = get_object_or_None(Group, name=data.group)
            if userGroup:
                oldUser.groups.add(userGroup)
            return CreateUser(user=oldUser)
        return DeleteGroup(message="Failed - Object Not found")


class DeleteUser(Mutation):
    class Arguments:
        id = ID(required=True)
    message = String()
    def mutate(root, info, id):
        oldUser = get_object_or_None(User, pk=id)
        if oldUser:
            oldUser.delete()
            return DeleteUser(message="Succes")
        return DeleteUser(message="Failed - Object Not found")


class Mutation(ObjectType):
#   token_auth = graphql_jwt.ObtainJSONWebToken.Field()
#   verify_token = graphql_jwt.Verify.Field()
#   refresh_token = graphql_jwt.Refresh.Field()
  createNationality = CreateNationality.Field()
  updateNationality = UpdateNationality.Field()
  deleteNationality = DeleteNationality.Field()
  createGroup = CreateGroup.Field()
  updateGroup = UpdateGroup.Field()
  deleteGroup = DeleteGroup.Field()
  createUser = CreateUser.Field()
  updateUser = UpdateUser.Field()
  deleteUser = DeleteUser.Field()