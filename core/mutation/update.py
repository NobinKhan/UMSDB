
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

