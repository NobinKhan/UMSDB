from graphene import ObjectType
from .create import CreateCourse, CreatePeriod, CreateShedule, CreateAssignCourse






class Mutation(ObjectType):
  createCourse = CreateCourse.Field()
  createPeriod = CreatePeriod.Field()
  createShedule = CreateShedule.Field()
  createAssignCourse = CreateAssignCourse.Field()
#   updateCourse = UpdateCourse.Field()
#   deleteCourse = DeleteCourse.Field()