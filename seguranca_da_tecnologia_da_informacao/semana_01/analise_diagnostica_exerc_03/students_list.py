from student import Student

class StudentList(object):
    def __init__(self) -> None:
        self.ls: dict[int, Student] = {}
        self.student_buffer: Student
        self.reg_buffer: int = 0

    def add(self, student: Student ):
        if self.reg_buffer >= 0:
            self.ls[ self.reg_buffer ] = student

    def remove(self, get_removed_item: bool = False):
        if self.reg_buffer >= 0:
            if get_removed_item == True:
                del self.ls[self.reg_buffer]
                return None
            return self.ls.pop(self.reg_buffer)

    def register(self, reg_number: int):
        self.reg_buffer = reg_number
        return self

    def get(self):
        if self.reg_buffer >= 0:
            return self.ls.get( self.reg_buffer )

    def print_list(self):
        buffer = self.ls.copy().items()
        for item in buffer:
            print( f'ID: {item[0]} => {item[1].name()} {item[1].last_name()} : {item[1].email()}' )
        print()


