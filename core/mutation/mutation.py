from graphene import ObjectType
from .create import CreateNationality, CreateDesignation, CreateGroup, CreateStudent, CreateTeacher, CreateStaff, CreateProfile, CreatePreviousEducation
from .update import UpdateNationality, UpdateDesignation, UpdateStudent, UpdateProfile, UpdateTeacher, UpdateStaff
# import graphql_jwt




class Mutation(ObjectType):
  createNationality = CreateNationality.Field()
  updateNationality = UpdateNationality.Field()
  createDesignation = CreateDesignation.Field()
  updateDesignation = UpdateDesignation.Field()
  createGroup = CreateGroup.Field()
  createStudent = CreateStudent.Field()
  updateStudent = UpdateStudent.Field()
  createTeacher = CreateTeacher.Field()
  updateTeacher = UpdateTeacher.Field()
  createStaff = CreateStaff.Field()
  updateStaff = UpdateStaff.Field()
  createProfile = CreateProfile.Field()
  updateProfile = UpdateProfile.Field()
  createPreviousEducation = CreatePreviousEducation.Field()


#   token_auth = graphql_jwt.ObtainJSONWebToken.Field()
#   verify_token = graphql_jwt.Verify.Field()
#   refresh_token = graphql_jwt.Refresh.Field()



# class DeleteUser(Mutation):
#     class Arguments:
#         id = ID(required=True)
#     message = String()
#     def mutate(root, info, id):
#         oldUser = get_object_or_None(User, pk=id)
#         if oldUser:
#             oldUser.delete()
#             return DeleteUser(message="Succes")
#         return DeleteUser(message="Failed - Object Not found")


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