
class UpdateCourseName(Mutation):
    class Arguments:
        id = ID(required=True)
        name = String()
        courseCode = Int()

    courseName = Field(CourseNameType)
    message = String()
    def mutate(root, info, id, name=None, courseCode=None):
        oldCourseName = get_object_or_None(CourseName, pk=id)
        if oldCourseName:
            if name:
                oldCourseName.name = name
            if courseCode:
                oldCourseName.code = courseCode
            oldCourseName.save()
            return UpdateCourseName(courseName=oldCourseName)
        return UpdateCourseName(message="Failed - Object Not found")



class UpdateCourse(Mutation):
    class Arguments:
        id = ID(required=True)
        courseName = ID()
        program = ID()

    course = Field(CourseType)
    message = String()
    def mutate(root, info, id, courseName=None, program=None):
        oldCourse = get_object_or_None(Course, pk=id)
        if oldCourse:
            if courseName:
                courseNameObject = get_object_or_None(CourseName, pk=courseName)
                if courseNameObject:
                    oldCourse.course = courseNameObject
            if program:
                programObject = get_object_or_None(Program, pk=program)
                if programObject:
                    oldCourse.program = programObject
            oldCourse.save()
            return UpdateCourse(course=oldCourse)
        return UpdateCourse(message="Failed - Object Not found")

