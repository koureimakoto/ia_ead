#!/usr/bin/env python3

from student import Student
from students_list import StudentList

def __init__():
    student_list: StudentList = StudentList()

    student_01 = Student()
    student_02 = Student()


    student_01.name('Talles')
    student_01.last_name('Fagundes')
    student_01.email('email@email.com')


    student_02.name('Carlos')
    student_02.last_name('Ferreira')
    student_02.email('emaildele@email.com')


    student_list.add(student_01).register('0101010')
    student_list.add(student_02).register('1010101')
    student_list.print_list()

__init__()