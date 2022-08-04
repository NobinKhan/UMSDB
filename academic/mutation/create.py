from graphene import String, Mutation, Field, Int, ID, List, InputObjectType, Time, Date, Float, Boolean
from functions.handle_error import get_object_or_None
from academic.models import Course, AssignCourse, Period, Shedule, Attendance, CourseResult, SemResult, AttendanceStatus
from layouts.models import Program, Department, Semester, Session
from academic.type import CourseType, AssignCourseType, PeriodType, SheduleType, AttendanceType, CourseResultType, SemResultType, AttendanceStatusType, CourseStatusType
from django.contrib.auth import get_user_model

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
        return CreateCourse(course=None)


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
    # studentIds = List(ID, required=True)


class CreateAssignCourse(Mutation):
    class Arguments:
        data = AssignCourseInput()

    assignCourse = Field(AssignCourseType)
    def mutate(root, info, data):
        sheduleObjects = Shedule.objects.filter(id__in=data.sheduleIds)
        semesterObject = get_object_or_None(Semester, pk=data.semesterId)
        sessionObject = get_object_or_None(Session, pk=data.sessionId)
        courseObject = get_object_or_None(Course, pk=data.courseId)
        teacherObject = get_object_or_None(get_user_model(), isTeacher=True, pk=data.teacherId)
        # studentObjects = Student.objects.filter(id__in=data.studentIds)
        if sheduleObjects and semesterObject and sessionObject and courseObject and teacherObject:
            newAssignCourse = AssignCourse(
                semester = semesterObject,
                session = sessionObject,
                course = courseObject,
                teacher = teacherObject,
            )
            newAssignCourse.save()
            newAssignCourse.shedule.set(sheduleObjects)
            # newAssignCourse.student.set(studentObjects) 
            return CreateAssignCourse(assignCourse=newAssignCourse)
        return CreateAssignCourse(assignCourse=None)


class CreateCourseStatus(Mutation):
    class Arguments:
        assignCourseId = ID(required=True)
        studentId = ID(required=True)
        retakeStatus = Boolean(required=True)

    courseStatus = Field(CourseStatusType)
    def mutate(root, info, assignCourseId, studentId, retakeStatus):
        assignCourseObject = get_object_or_None(AssignCourse, pk=assignCourseId)
        studentObject = get_object_or_None(get_user_model(), isStudent=True, pk=studentId)
        if assignCourseObject and studentObject:
            newCourseStatus = CourseStatus(
                assignCourse = assignCourseObject,
                student = studentObject,
                retake = retakeStatus,
            )
            newCourseStatus.save()
            return CreateCourseStatus(courseStatus=newCourseStatus)
        return CreateCourseStatus(courseStatus=None)


class AttendanceInput(InputObjectType):
    assignCourseId = ID(required=True)
    date = Date(required=True)
    sheduleId = ID(required=True)


class CreateAttendance(Mutation):
    class Arguments:
        data = AttendanceInput()

    attendance = Field(AttendanceType)
    def mutate(root, info, data):
        sheduleObject = get_object_or_None(Shedule, pk=data.sheduleId)
        assignCourseObject = get_object_or_None(AssignCourse, pk=data.assignCourseId)
        sheduleObjects = assignCourseObject.shedule.all()
        if sheduleObject in sheduleObjects and data.date:
            newAttendance = Attendance(
                shedule = sheduleObject,
                assignCourse = assignCourseObject,
                attendenceDate = data.date,
            )
            newAttendance.save()
            return CreateAttendance(attendance=newAttendance)
        return CreateAttendance(attendance=None)


class AttendanceStatusInput(InputObjectType):
    attendanceId = ID(required=True)
    studentId = ID(required=True)
    status = String(required=True)


class CreateAttendanceStatus(Mutation):
    class Arguments:
        data = AttendanceStatusInput()

    attendanceStatus = Field(AttendanceStatusType)
    def mutate(root, info, data):
        studentObject = get_object_or_None(Student, pk=data.studentId)
        attendanceObject = get_object_or_None(Attendance, pk=data.attendanceId)
        studentObjects = attendanceObject.assignCourse.student.all()
        if data.status in [d[0] for d in AttendanceStatus.attendanceChoices] and studentObject in studentObjects:
            newAttendanceStatus = AttendanceStatus(
                student = studentObject,
                attendance = attendanceObject,
                status = data.status,
            )
            newAttendanceStatus.save()
            return CreateAttendanceStatus(attendanceStatus=newAttendanceStatus)
        return CreateAttendanceStatus(attendanceStatus=None)


class CourseResultInput(InputObjectType):
    assignCourseId = ID(required=True)
    studentId = ID(required=True)
    creditHours = Float(required=True)
    midMark = Float(required=True)


class CreateCourseResult(Mutation):
    class Arguments:
        data = CourseResultInput()

    courseResult = Field(CourseResultType)
    def mutate(root, info, data):
        studentObject = get_object_or_None(Student, pk=data.studentId)
        assignCourseObject = get_object_or_None(AssignCourse, pk=data.assignCourseId)
        # studentObjects = attendanceObject.assignCourse.student.all()
        # if data.status in [d[0] for d in CourseResult.attendanceChoices] and studentObject in studentObjects:
        if studentObject and assignCourseObject:
            newCourseResult = CourseResult(
                assignCourse = assignCourseObject,
                student = studentObject,
                creditHours = data.creditHours,
                midMark = data.midMark,
            )
            newCourseResult.save()
            return CreateCourseResult(courseResult=newCourseResult)
        return CreateCourseResult(courseResult=None)





# print("*************\n \n ")
# print(sheduleObject)
# print(obj)
# if sheduleObject in obj:
#     print(True)
# print("\n \n*************")
#    [Shedule.dayChoice[d][0] for d in range(len(Shedule.dayChoice))] is same as [d[0] for d in Shedule.day.field.choices]