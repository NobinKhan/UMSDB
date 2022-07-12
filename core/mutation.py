from django.contrib.auth.models import Group
from functions.handle_error import get_object_or_None
from layouts.models import Semester, Session, Program, Department
from .models import User, Nationality, Designation, Profile, PreviousEducation
from graphene import InputObjectType, String, Mutation, Field, Date, Int, ObjectType, Float, ID
from .type import UserType, GroupType, NationalityType, ProfileType, DesignationType, PreviousEducationType
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


class CreateDesignation(Mutation):
    class Arguments:
        name = String(required=True)
    designation = Field(DesignationType)
    def mutate(root, info, name):
        newDesignation = Designation(name = name)
        newDesignation.save()
        return CreateDesignation(designation=newDesignation)


class UpdateDesignation(Mutation):
    class Arguments:
        id = ID(required=True)
        name = String(required=True)
    designation = Field(DesignationType)
    message = String()
    def mutate(root, info, name, id):
        oldDesignation = get_object_or_None(Designation, pk=id)
        if oldDesignation:
            oldDesignation.name = name
            oldDesignation.save()
            return UpdateDesignation(designation=oldDesignation)
        return UpdateDesignation(message="Failed - Object Not found")


class CreateGroup(Mutation):
    class Arguments:
        name = String(required=True)
    group = Field(GroupType)
    def mutate(root, info, name):
        newGroup = Group(name = name)
        newGroup.save()
        return CreateGroup(group=newGroup)


class CreateStudentInput(InputObjectType):
    email = String(required=True)
    dateOfBirth = Date(required=True)
    gender = String(required=True)
    joiningSessionID = ID(required=True)
    designationID = ID(required=True)
    studentType = String(required=True)
    programID = ID(required=True)
    joiningSemesterID = ID(required=True)
    password = String(required=True)
    groupID = ID(required=True)


class CreateStudent(Mutation):
    class Arguments:
        data = CreateStudentInput()
    student = Field(UserType)
    def mutate(root, info, data=None):
        sessionInstance = get_object_or_None(Session, pk=data.joiningSessionID)
        programInstance = get_object_or_None(Program, pk=data.programID)
        semesterInstance = get_object_or_None(Semester, pk=data.joiningSemesterID)
        designationInstance = get_object_or_None(Designation, pk=data.designationID)
        if sessionInstance and programInstance and semesterInstance and designationInstance:
            newStudent = User(
                email = data.email,
                date_of_birth = data.dateOfBirth,
                gender = data.gender,
                joinedSession= sessionInstance,
                isStudent=True,
                studentAddmissionType=data.studentType,
                program=programInstance,
                joinedSemester=semesterInstance,
                designation=designationInstance,
            )
            newStudent.set_password(data.password)
            newStudent.save()
            userGroup = get_object_or_None(Group, pk=data.groupID)
            grp = Group.objects.filter(user = newStudent)
            if userGroup and not grp:
                newStudent.groups.add(userGroup)
            return CreateStudent(student=newStudent)


class CreateTeacherInput(InputObjectType):
    email = String(required=True)
    dateOfBirth = Date(required=True)
    gender = String(required=True)
    joiningSessionID = ID(required=True)
    designationID = ID(required=True)
    departmentID = ID(required=True)
    password = String(required=True)
    groupID = ID(required=True)


class CreateTeacher(Mutation):
    class Arguments:
        data = CreateTeacherInput()
    teacher = Field(UserType)
    def mutate(root, info, data=None):
        sessionInstance = get_object_or_None(Session, pk=data.joiningSessionID)
        departmentInstance = get_object_or_None(Department, pk=data.departmentID)
        designationInstance = get_object_or_None(Designation, pk=data.designationID)
        if sessionInstance and departmentInstance and designationInstance:
            newTeacher = User(
                email = data.email,
                date_of_birth = data.dateOfBirth,
                gender = data.gender,
                joinedSession= sessionInstance,
                isTeacher=True,
                department=departmentInstance,
                designation=designationInstance,
            )
            newTeacher.set_password(data.password)
            newTeacher.save()
            userGroup = get_object_or_None(Group, pk=data.groupID)
            grp = Group.objects.filter(user = newTeacher)
            if userGroup and not grp:
                newTeacher.groups.add(userGroup)
            return CreateTeacher(teacher=newTeacher)


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
                oldUser.groups.clear()
                oldUser.groups.add(userGroup)
                # grp = Group.objects.filter(user = oldUser)
                # if not grp:
                #     print("group found maybe")
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


class CreateProfileInput(InputObjectType):
    firstName = String(required=True)
    lastName = String(required=True)
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


class Mutation(ObjectType):
  createNationality = CreateNationality.Field()
  updateNationality = UpdateNationality.Field()
  createDesignation = CreateDesignation.Field()
  createGroup = CreateGroup.Field()
  createStudent = CreateStudent.Field()
  createTeacher = CreateTeacher.Field()
  updateUser = UpdateUser.Field()
  deleteUser = DeleteUser.Field()


#   token_auth = graphql_jwt.ObtainJSONWebToken.Field()
#   verify_token = graphql_jwt.Verify.Field()
#   refresh_token = graphql_jwt.Refresh.Field()

        # username = data.userName,
        # first_name = data.firstName,
        # last_name = data.lastName,
        # permanentAddress = data.permanentAddress,
        # presentAddress = data.presentAddress,
        # mobilePhone = data.mobilePhone,
        # mobilePhone2 = data.mobilePhone2,
        # nid = data.nid,
        # birthCertNumber = data.birthCertNumber,
        # nationality = nationalityInstance,
        # fatherName = data.fatherName,
        # motherName = data.motherName,
        # photo = data.photo,



# class DeleteNationality(Mutation):
#     class Arguments:
#         id = ID(required=True)
#     message = String()
#     def mutate(root, info, id):
#         oldNationality = get_object_or_None(Nationality, pk=id)
#         if oldNationality:
#             oldNationality.delete()
#             return DeleteNationality(message="Succes")
#         return DeleteNationality(message="Failed - Object Not found")


# class UpdateGroup(Mutation):
#     class Arguments:
#         id = ID(required=True)
#         name = String(required=True)
#     group = Field(GroupType)
#     message = String()
#     def mutate(root, info, name, id):
#         oldGroup = get_object_or_None(Group, pk=id)
#         if oldGroup:
#             oldGroup.name = name
#             oldGroup.save()
#             return UpdateGroup(group=oldGroup)
#         return UpdateGroup(message="Failed - Object Not found")


# class DeleteGroup(Mutation):
#     class Arguments:
#         id = ID(required=True)
#     message = String()
#     def mutate(root, info, id):
#         oldGroup = get_object_or_None(Group, pk=id)
#         if oldGroup:
#             oldGroup.delete()
#             return DeleteGroup(message="Succes")
#         return DeleteGroup(message="Failed - Object Not found")