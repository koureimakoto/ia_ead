#!/usr/bin/env python3

from student import Student
from students_list import StudentList

def __init__():
    student_list: StudentList = StudentList()

    student_01: Student = Student()
    student_02: Student = Student()
    student_03: Student = Student()
    student_04: Student = Student()
    student_05: Student = Student()

    student_01.name('Talles')
    student_01.last_name('Fagundes')
    student_01.email('email@email.com')


    student_02.name('Carlos')
    student_02.last_name('Ferreira')
    student_02.email('emaildele@email.com')

    student_03.name('Lucia')
    student_03.last_name('de Oliveira')
    student_03.email('emaildela@email.com')

    student_04.name('Cacatua')
    student_04.last_name('Topetuda')
    student_04.email('emailit@email.com')

    student_05.name('Luana')
    student_05.last_name('Piamuito')
    student_05.email('bird@email.com')


    student_list.register(1111).add(student_01)
    student_list.register(1110).add(student_02)
    student_list.register(1101).add(student_03)
    student_list.register(1011).add(student_04)
    student_list.register(1100).add(student_05)
    student_list.print_list()
    


# __INIT__
__init__()