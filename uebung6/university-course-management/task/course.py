#!/usr/bin/env python3

from professor import Professor
from student import Student


class Course:

    def __init__(self, course_code: str, course_name: str, professor: Professor):
        self.course_code = course_code
        self.course_name = course_name
        self.professor = professor
        self.students = []

    def add_student(self, student: Student) -> int:
        if student in self.students:
            raise ValueError
        self.students.append(student)
        return len(self.students)

    def get_students(self) -> list:
        return[b.get_details() for b in self.students]

    def remove_student(self, student_id: str) -> int:
        for student in self.students:
            if student_id == student.student_id:
                self.students.remove(student)
                return len(self.students)
        raise ValueError

    def get_details(self) -> tuple:
        return((self.course_code, self.course_name, self.professor.get_details(), len(self.students)))
