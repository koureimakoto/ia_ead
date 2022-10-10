from student import Student

class StudentList(object):
    def __init__(self) -> None:
        self.list: dict[str, Student] = {}
        self.student_buffer: Student
        self.reg_buffer: str = ''

    def add(self, student: Student ):
        self.student_buffer = student
        return self

    def remove(self):
        del self.list[self.reg_buffer]
        pass

    def register(self, reg_mumber: str):
        self.list[reg_mumber] = self.student_buffer
        del self.student_buffer

    def get(self):
        return self.list

    def print_list(self):
        print( self.list )

    def __str__(self):
        return self.sequence + '.'

