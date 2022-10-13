from re import A
from typing import overload


class Student:
    def __init__(self, name: str = '', last_name: str = '', email: str = '') -> None:
        self.data = [ 
            name,
            last_name,
            email
        ]
        self.name_size     : int = 0
        self.last_name_size: int = 0

    """
    Testando a utilização de chamadas via argumentos
    Quero testar ainda usando __call__
    """
    # __NAME__
    def name(self, *args, **kwargs):
        size_args  : int = len(args)
        size_kwargs: int = len(kwargs)
        if size_args == 0 and size_kwargs == 0:
            return self.gname()
        else:
            return self.sname(*args, **kwargs)


    def sname(self, name: str):
        if name == '':
            return False
        self.name_size = len(name)
        self.data[0] = name
        return True

    def gname(self):
        return self.data[0]


    # __LAST_NAME__
    def last_name(self, *args, **kwargs):
        size_args  : int = len(args)
        size_kwargs: int = len(kwargs)
        if size_args == 0 and size_kwargs == 0:
            return self.glast_name()
        else:
            return self.slast_name(*args, **kwargs)

    def slast_name(self, last_name: str):
        if last_name == '':
            return False
        self.last_name_size = len(last_name)
        self.data[1] = last_name
        return True
    
    def glast_name(self):
        return self.data[1]

    # __EMAIL__
    def email(self, *args, **kwargs):
        size_args  : int = len(args)
        size_kwargs: int = len(kwargs)
        if size_args == 0 and size_kwargs == 0:
            return self.gemail()
        else:
            return self.semail(*args, **kwargs)
    
    def semail(self, email: str):
        if email == '':
            return False
        self.data[2] = email
        return True
    
    def gemail(self):
        return self.data[2]

    def size(self):
        return self.name_size + self.last_name_size