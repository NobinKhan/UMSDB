from graphene import ObjectType
from .create import CreateCourse, CreatePeriod, CreateShedule, CreateAssignCourse, CreateAttendance, CreateAttendanceStatus






class Mutation(ObjectType):
  createCourse = CreateCourse.Field()
  createPeriod = CreatePeriod.Field()
  createShedule = CreateShedule.Field()
  createAssignCourse = CreateAssignCourse.Field()
  createAttendance = CreateAttendance.Field()
  createAttendanceStatus = CreateAttendanceStatus.Field()
#   updateCourse = UpdateCourse.Field()
#   deleteCourse = DeleteCourse.Field()