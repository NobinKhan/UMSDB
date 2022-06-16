from graphene import String, Mutation, Field, Int, ID, List, InputObjectType, Time
from functions.handle_error import get_object_or_None
from academic.models import Course, AssignCourse, Period, Shedule, Attendance, CourseResult, SemResult
from teacher.models import Teacher
from student.models import Student
from layouts.models import Program, Department, Semester, Session
from academic.type import CourseType, AssignCourseType, PeriodType, SheduleType, AttendanceType, CourseResultType, SemResultType


class CourseInput(InputObjectType):
    courseName = String(required=True)
    courseCode = String(required=True)
    underDepartment = ID(required=True)
    programIds = List(ID, required=True)


class CreateCourse(Mutation):
    class Arguments:
        data = CourseInput()

    course = Field(CourseType)
    def mutate(root, info, data=None):
        departmentObject = get_object_or_None(Department, pk=data.underDepartment)
        # programObjects = Program.objects.filter(id__in=programIds).values_list('id', flat=True)
        programObjects = Program.objects.filter(id__in=data.programIds)
        if data.underDepartment and programObjects:
            newCourse = Course(
                name=data.courseName,
                code=data.courseCode,
                department=departmentObject,
            )
            newCourse.save()
            newCourse.program.set(programObjects)
        return CreateCourse(course=newCourse)


class CreatePeriod(Mutation):
    class Arguments:
        startTime = Time(required=True)
        endTime = Time(required=True)

    period = Field(PeriodType)
    def mutate(root, info, startTime, endTime):
        newPeriod = Period(
            startTime=startTime,
            endTime=endTime,
        )
        newPeriod.save()
        return CreatePeriod(period=newPeriod)


class CreateShedule(Mutation):
    class Arguments:
        day = String(required=True)
        periodId = ID(required=True)

    shedule = Field(SheduleType)
    def mutate(root, info, day, periodId):
        periodObject = get_object_or_None(Period, pk=periodId)
        if day in [d[0] for d in Shedule.dayChoice] and periodObject:
            newShedule = Shedule(
                day=day,
                period=periodObject,
            )
            newShedule.save()
            return CreateShedule(shedule=newShedule)
        return CreateShedule(shedule=None)


class AssignCourseInput(InputObjectType):
    sheduleIds = List(ID, required=True)
    semesterId = ID(required=True)
    sessionId = ID(required=True)
    courseId = ID(required=True)
    teacherId = ID(required=True)
    studentIds = List(ID, required=True)


class CreateAssignCourse(Mutation):
    class Arguments:
        data = AssignCourseInput()

    assignCourse = Field(AssignCourseType)
    def mutate(root, info, data):
        sheduleObjects = Shedule.objects.filter(id__in=data.sheduleIds)
        semesterObject = get_object_or_None(Semester, pk=data.semesterId)
        sessionObject = get_object_or_None(Session, pk=data.sessionId)
        courseObject = get_object_or_None(Course, pk=data.courseId)
        teacherObject = get_object_or_None(Teacher, pk=data.teacherId)
        studentObjects = Student.objects.filter(id__in=data.studentIds)
        print(sheduleObjects, semesterObject, sessionObject, courseObject, teacherObject, studentObjects)
        if sheduleObjects and semesterObject and sessionObject and courseObject and teacherObject and studentObjects:
            newAssignCourse = AssignCourse(
                semester = semesterObject,
                session = sessionObject,
                course = courseObject,
                teacher = teacherObject,
            )
            newAssignCourse.save()
            newAssignCourse.shedule.set(sheduleObjects)
            newAssignCourse.student.set(studentObjects) 
            return CreateAssignCourse(assignCourse=newAssignCourse)
        return CreateAssignCourse(assignCourse=None)


        # print("*************\n \n ")
    #    [Shedule.dayChoice[d][0] for d in range(len(Shedule.dayChoice))] is same as [d[0] for d in Shedule.day.field.choices]