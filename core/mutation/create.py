from django.contrib.auth.models import Group
from functions.handle_error import get_object_or_None
from layouts.models import Semester, Session, Program, Department
from core.models import User, Nationality, Designation, Profile, PreviousEducation
from graphene import InputObjectType, String, Mutation, Field, Date, Int, Float, ID
from core.type import UserType, GroupType, NationalityType, ProfileType, DesignationType, PreviousEducationType



class CreateNationality(Mutation):
    class Arguments:
        name = String(required=True)
    nationality = Field(NationalityType)
    def mutate(root, info, name):
        newNationality = Nationality(name = name)
        newNationality.save()
        return CreateNationality(nationality=newNationality)


class CreateDesignation(Mutation):
    class Arguments:
        name = String(required=True)
    designation = Field(DesignationType)
    def mutate(root, info, name):
        newDesignation = Designation(name = name)
        newDesignation.save()
        return CreateDesignation(designation=newDesignation)


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
        if data.studentType in [d[0] for d in User.typeChoices] and data.gender in [d[0] for d in User.genderChoices]:
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
        return None


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
        if data.gender in [d[0] for d in User.genderChoices]:
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
        return None


class CreateStaffInput(InputObjectType):
    email = String(required=True)
    dateOfBirth = Date(required=True)
    gender = String(required=True)
    joiningSessionID = ID(required=True)
    designationID = ID(required=True)
    password = String(required=True)
    groupID = ID(required=True)


class CreateStaff(Mutation):
    class Arguments:
        data = CreateStaffInput()
    staff = Field(UserType)
    def mutate(root, info, data=None):
        if data.gender in [d[0] for d in User.genderChoices]:
            sessionInstance = get_object_or_None(Session, pk=data.joiningSessionID)
            designationInstance = get_object_or_None(Designation, pk=data.designationID)
            if sessionInstance and designationInstance:
                newStaff = User(
                    email = data.email,
                    date_of_birth = data.dateOfBirth,
                    gender = data.gender,
                    joinedSession= sessionInstance,
                    is_staff=True,
                    designation=designationInstance,
                )
                newStaff.set_password(data.password)
                newStaff.save()
                userGroup = get_object_or_None(Group, pk=data.groupID)
                grp = Group.objects.filter(user = newStaff)
                if userGroup and not grp:
                    newStaff.groups.add(userGroup)
                return CreateStaff(staff=newStaff)
        return None


class CreateProfileInput(InputObjectType):
    userID = ID(required=True)
    firstName = String(required=True)
    lastName = String(required=True)
    permanentAddress = String(required=True)
    presentAddress = String(required=True)
    mobilePhone = String(required=True)
    mobilePhone2 = String(required=True)
    nid = Float()
    birthCertNumber = Float(required=True)
    nationalityID = ID(required=True)
    fatherName = String(required=True)
    motherName = String(required=True)
    photo = String(required=True)


class CreateProfile(Mutation):
    class Arguments:
        data = CreateProfileInput()
    profile = Field(ProfileType)
    def mutate(root, info, data=None):
        Profile.phone_regex(data.mobilePhone)
        Profile.phone_regex(data.mobilePhone2)
        userInstance = get_object_or_None(User, pk=data.userID)
        nationalityInstance = get_object_or_None(Nationality, pk=data.nationalityID)
        if userInstance and nationalityInstance:
            newProfile = Profile(
                user=userInstance,
                first_name = data.firstName,
                last_name = data.lastName,
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
            newProfile.save()
            return CreateProfile(profile=newProfile)


class CreatePreviousEducationInput(InputObjectType):
    userID = ID(required=True)
    sscName = String(required=True)
    sscGpa = Float(required=True)
    sscYear = Int(required=True)
    sscCertFile = String(required=True)
    hscName = String(required=True)
    hscGpa = Float(required=True)
    hscYear = Int(required=True)
    hscCertFile = String(required=True)
    bscName = String()
    bscInstitute = String()
    bscGpa = Float()
    bscYear = Int()
    bscCertFile = String()
    mscName = String()
    mscInstitute = String()
    mscGpa = Float()
    mscYear = Int()
    mscCertFile = String()
    phdName = String()
    phdInstitute = String()
    phdGpa = Float()
    phdYear = Int()
    phdCertFile = String()


class CreatePreviousEducation(Mutation):
    class Arguments:
        data = CreatePreviousEducationInput()
    previousEducation = Field(PreviousEducationType)
    def mutate(root, info, data=None):
        if data.sscName in [d[0] for d in PreviousEducation.ssceqChoices] and data.hscName in [d[0] for d in PreviousEducation.hsceqChoices]:
            userInstance = get_object_or_None(User, pk=data.userID)
            if userInstance:
                newPreviousEducation = PreviousEducation(
                    user=userInstance,
                    ssceq = data.sscName,
                    sscGpa = data.sscGpa,
                    sscYear = data.sscYear,
                    sscFile = data.sscCertFile,
                    hsceq = data.hscName,
                    hscGpa = data.hscGpa,
                    hscYear = data.hscYear,
                    hscfile = data.hscCertFile,
                    bachelor=data.bscName,
                    bscInstitute=data.bscInstitute,
                    bachelorGpa=data.bscGpa,
                    bachelorYear=data.bscYear,
                    bachelorFile=data.bscCertFile,
                    master=data.mscName,
                    mscInstitute=data.mscInstitute,
                    masterGpa=data.mscGpa,
                    masterYear=data.mscYear,
                    masterFile=data.mscCertFile,
                    phd=data.phdName,
                    phdInstitute=data.phdInstitute,
                    phdGpa=data.phdGpa,
                    phdYear=data.phdYear,
                    phdFile=data.phdCertFile,
                )
                newPreviousEducation.save()
                return CreatePreviousEducation(previousEducation=newPreviousEducation)

