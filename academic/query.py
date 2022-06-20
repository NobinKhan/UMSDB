from graphene import ObjectType, List, Int, String, Float
from .models import Course, AssignCourse, Period, Shedule, Attendance, CourseResult, SemResult, AttendanceStatus
from .type import CourseType, AssignCourseType, PeriodType, SheduleType, AttendanceType, CourseResultType, SemResultType, AttendanceStatusType



class Query(ObjectType):
    course = List(CourseType, id=Int())
    assignCourse = List(AssignCourseType, id=Int())
    period = List(PeriodType, id=Int())
    Shedule = List(SheduleType, id=Int())
    attendance = List(AttendanceType, id=Int())
    attendanceStatus = List(AttendanceStatusType, id=Int())
    courseResult = List(CourseResultType, id=Int())
    semResult = List(SemResultType, id=Int())


    def resolve_course(self, info, id=None):
        if id:
            return Course.objects.filter(pk=id)
        return Course.objects.all()
    
    def resolve_assignCourse(self, info, id=None):
        if id:
            return AssignCourse.objects.filter(pk=id)
        return AssignCourse.objects.all()
    
    def resolve_period(self, info, id=None):
        if id:
            return Period.objects.filter(pk=id)
        return Period.objects.all()
    
    def resolve_Shedule(self, info, id=None):
        if id:
            return Shedule.objects.filter(pk=id)
        return Shedule.objects.all()
    
    def resolve_attendance(self, info, id=None):
        if id:
            return Attendance.objects.filter(pk=id)
        return Attendance.objects.all()

    def resolve_attendanceStatus(self, info, id=None):
        if id:
            return AttendanceStatus.objects.filter(pk=id)
        return AttendanceStatus.objects.all()
    
    def resolve_courseResult(self, info, id=None):
        if id:
            return CourseResult.objects.filter(pk=id)
        return CourseResult.objects.all()

    def resolve_semResult(self, info, id=None):
        if id:
            return SemResult.objects.filter(pk=id)
        return SemResult.objects.all()