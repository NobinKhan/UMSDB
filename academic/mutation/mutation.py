from graphene import ObjectType
from .create import (
  CreateCourse, 
  CreatePeriod, 
  CreateShedule, 
  CreateAssignCourse, 
  CreateAttendance, 
  CreateAttendanceStatus, 
  CreateCourseResult, 
  CreateCourseStatus
)






class Mutation(ObjectType):
  createCourse = CreateCourse.Field()
  createPeriod = CreatePeriod.Field()
  createShedule = CreateShedule.Field()
  createAssignCourse = CreateAssignCourse.Field()
  createAttendance = CreateAttendance.Field()
  createAttendanceStatus = CreateAttendanceStatus.Field()
  createCourseResult = CreateCourseResult.Field()
  createCourseStatus = CreateCourseStatus.Field()
#   updateCourse = UpdateCourse.Field()
#   deleteCourse = DeleteCourse.Field()