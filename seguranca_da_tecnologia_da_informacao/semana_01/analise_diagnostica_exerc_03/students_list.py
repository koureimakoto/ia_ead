from student import Student

class StudentList(object):
    def __init__(self) -> None:
        self.ls: dict[int, Student] = {}
        self.student_buffer: Student
        self.reg_buffer    : int = 0

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
        max_width: int = self.max_width()
        width    : int = 0
        for item in buffer:
            width = item[1].size()
            print( f'ID: {item[0]} => {item[1].name()} {item[1].last_name()}{self.space(width, max_width)} : {item[1].email()}' )
        print()

    def max_width(self):
        buffer = self.ls.copy().items()
        size     : int = 0
        last_size: int = 0
        for item in buffer:
            size = item[1].size() 
            if size > last_size:
                last_size = size
        return last_size

    def space(self, width: int, max_width: int):
        space: str = ' '
        while width < max_width:
            width += 1
            space += ' '
        return space

