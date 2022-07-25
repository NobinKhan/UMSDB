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


class UpdateStudentInput(InputObjectType):
    id = ID(required=True)
    email = String()
    dateOfBirth = Date()
    gender = String()
    joiningSessionID = ID()
    designationID = ID()
    studentType = String()
    programID = ID()
    joiningSemesterID = ID()
    password = String()
    groupID = ID()


class UpdateStudent(Mutation):
    class Arguments:
        data = UpdateStudentInput()
    student = Field(UserType)
    def mutate(root, info, data=None):
        oldStudent = get_object_or_None(User, pk=data.id, isStudent=True)
        if not oldStudent:
            return None
        if data.studentType and data.gender:
            if data.studentType in [d[0] for d in User.typeChoices] and data.gender in [d[0] for d in User.genderChoices]:
                oldStudent.gender = data.gender
                oldStudent.studentAddmissionType = data.studentType
        sessionInstance = get_object_or_None(Session, pk=data.joiningSessionID)
        if sessionInstance:
            oldStudent.joinedSession = sessionInstance
        programInstance = get_object_or_None(Program, pk=data.programID)
        if programInstance:
            oldStudent.program = programInstance
        semesterInstance = get_object_or_None(Semester, pk=data.joiningSemesterID)
        if semesterInstance:
            oldStudent.joinedSemester = semesterInstance
        designationInstance = get_object_or_None(Designation, pk=data.designationID)
        if designationInstance:
            oldStudent.designation = designationInstance
        if data.email:
            oldStudent.email = data.email
        if data.dateOfBirth:
            oldStudent.date_of_birth = data.dateOfBirth
        if data.password:
            oldStudent.set_password(data.password)
        oldStudent.save()
        userGroup = get_object_or_None(Group, pk=data.groupID)
        grp = Group.objects.filter(user = oldStudent)
        if userGroup and not grp:
            oldStudent.groups.add(userGroup)
        return UpdateStudent(student=oldStudent)


class UpdateTeacherInput(InputObjectType):
    id = ID(required=True)
    email = String()
    dateOfBirth = Date()
    gender = String()
    joiningSessionID = ID()
    designationID = ID()
    departmentID = ID()
    password = String()
    groupID = ID()


class UpdateTeacher(Mutation):
    class Arguments:
        data = UpdateTeacherInput()
    teacher = Field(UserType)
    def mutate(root, info, data=None):
        oldTeacher = get_object_or_None(User, pk=data.id, isTeacher=True)
        if not oldTeacher:
            return None
        if data.gender:
            if data.gender in [d[0] for d in User.genderChoices]:
                oldTeacher.gender = data.gender
        sessionInstance = get_object_or_None(Session, pk=data.joiningSessionID)
        if sessionInstance:
            oldTeacher.joinedSession = sessionInstance
        departmentInstance = get_object_or_None(Department, pk=data.departmentID)
        if departmentInstance:
            oldTeacher.department = departmentInstance
        designationInstance = get_object_or_None(Designation, pk=data.designationID)
        if designationInstance:
            oldTeacher.designation = designationInstance
        if data.email:
            oldTeacher.email = data.email
        if data.dateOfBirth:
            oldTeacher.date_of_birth = data.dateOfBirth
        if data.password:
            oldTeacher.set_password(data.password)
        oldTeacher.save()
        userGroup = get_object_or_None(Group, pk=data.groupID)
        grp = Group.objects.filter(user = oldTeacher)
        if userGroup and not grp:
            oldTeacher.groups.add(userGroup)
        return UpdateTeacher(teacher=oldTeacher)


class UpdateStaffInput(InputObjectType):
    id = ID(required=True)
    email = String()
    dateOfBirth = Date()
    gender = String()
    joiningSessionID = ID()
    designationID = ID()
    password = String()
    groupID = ID()


class UpdateStaff(Mutation):
    class Arguments:
        data = UpdateStaffInput()
    staff = Field(UserType)
    def mutate(root, info, data=None):
        oldStaff = get_object_or_None(User, pk=data.id, is_staff=True)
        if not oldStaff:
            return None
        if data.gender:
            if data.gender in [d[0] for d in User.genderChoices]:
                oldStaff.gender = data.gender
        sessionInstance = get_object_or_None(Session, pk=data.joiningSessionID)
        if sessionInstance:
            oldStaff.joinedSession = sessionInstance
        designationInstance = get_object_or_None(Designation, pk=data.designationID)
        if designationInstance:
            oldStaff.designation = designationInstance
        if data.email:
            oldStaff.email = data.email
        if data.dateOfBirth:
            oldStaff.date_of_birth = data.dateOfBirth
        if data.password:
            oldStaff.set_password(data.password)
        oldStaff.save()
        userGroup = get_object_or_None(Group, pk=data.groupID)
        grp = Group.objects.filter(user = oldStaff)
        if userGroup and not grp:
            oldStaff.groups.add(userGroup)
        return UpdateStaff(staff=oldStaff)


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
            oldProfile.save()
            return UpdateProfile(profile=oldProfile)

