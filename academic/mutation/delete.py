
class DeleteCourseName(Mutation):
    class Arguments:
        id = ID(required=True)
    message = String()
    def mutate(root, info, id):
        oldCourseName = get_object_or_None(CourseName, pk=id)
        if oldCourseName:
            oldCourseName.delete()
            return DeleteCourseName(message="Succes")
        return DeleteCourseName(message="Failed - Object Not found")


class DeleteCourse(Mutation):
    class Arguments:
        id = ID(required=True)
    message = String()
    def mutate(root, info, id):
        oldCourse = get_object_or_None(Course, pk=id)
        if oldCourse:
            oldCourse.delete()
            return DeleteCourse(message="Succes")
        return DeleteCourse(message="Failed - Object Not found")


