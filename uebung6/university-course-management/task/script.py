#!/usr/bin/env python3

# The purpose of this file is illustrating the class usages. This script
# is irrelevant for the grading and you can freely change its contents.

from student import Student
from professor import Professor
from course import Course

student01 = Student("Alice", "alice@uzh.ch", "24-000-001")
student02 = Student("Bob", "bob@uzh.ch", "24-000-002")
student03 = Student("Charlie", "charlie@uzh.ch", "24-000-003")
print(student01.get_details())

professor = Professor("Dr. Dave", "dave@uzh.ch", "01234567", "BIN-0.Z.00")
print(professor.get_details())

course = Course("CS999", "Daveology 101", professor)
print(course.get_details())

course.add_student(student01)
course.add_student(student02)
course.add_student(student03)
print(course.get_details())
print(course.get_students())

course.remove_student("24-000-003")
print(course.get_details())
print(course.get_students())