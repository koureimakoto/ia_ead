from student import Student

class StudentList:
    def __init__(self) -> None:
        self.list: dict[str, Student] = {}
        self.student_buffer: Student

    def add(self, student: Student ):
        self.student_buffer = student
        return self

    def register(self, reg_mumber: str):
        self.list[reg_mumber] = self.student_buffer
        del self.student_buffer
        pass

    def print_list(self):
        print( self.list )

