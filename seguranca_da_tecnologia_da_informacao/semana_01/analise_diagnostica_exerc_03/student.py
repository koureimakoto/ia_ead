"""
Student
    __init__
    name
    email
    last_name
    __(s|g)name
    __(s|g)email
    __(s|g)last_name
"""
class Student:
    def __init__(
        self,
        name      : str = '',
        last_name : str = '',
        email     : str = ''
        ) -> None:
        self.data: list[str] = [ 
            name,
            last_name,
            email
        ]
        self.name_size     : int = 0
        self.last_name_size: int = 0

    """
    Testando a utilização de chamadas via argumentos
    """
    # __NAME__
    # Get ou Set the student name inside class
    def name(self, *args, **kwargs):
        size_args  : int = len(args)
        size_kwargs: int = len(kwargs)
        if size_args == 0 and size_kwargs == 0:
            return self.__gname()
        else:
            return self.__sname(*args, **kwargs)

    # Private Set name
    def __sname(self, name: str):
        if name == '':
            return False
        self.name_size = len(name)
        self.data[0] = name
        return True

    # Private Get Name
    def __gname(self):
        return self.data[0]

    # __LAST_NAME__
    # Get ou Set the student last name inside class
    def last_name(self, *args, **kwargs):
        size_args  : int = len(args)
        size_kwargs: int = len(kwargs)
        if size_args == 0 and size_kwargs == 0:
            return self.__glast_name()
        else:
            return self.__slast_name(*args, **kwargs)

    # Private Set last name
    def __slast_name(self, last_name: str):
        if last_name == '':
            return False
        self.last_name_size = len(last_name)
        self.data[1] = last_name
        return True
    
    # Private Get last name
    def __glast_name(self):
        return self.data[1]

    # __EMAIL__
    # Get ou Set the student e-mail inside class
    def email(self, *args, **kwargs):
        size_args  : int = len(args)
        size_kwargs: int = len(kwargs)
        if size_args == 0 and size_kwargs == 0:
            return self.__gemail()
        else:
            return self.__semail(*args, **kwargs)
    
    # Private set e-mail
    def __semail(self, email: str):
        if email == '':
            return False
        self.data[2] = email
        return True
    
    # Private get e-mail
    def __gemail(self):
        return self.data[2]

    # Full name size
    def size(self):
        return self.name_size + self.last_name_size