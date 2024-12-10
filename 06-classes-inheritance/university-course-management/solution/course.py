#!/usr/bin/env python3

from task.professor import Professor
from task.student import Student


class Course:

    def __init__(self, course_code: str, course_name: str, professor: Professor):
        self.course_code = course_code
        self.course_name = course_name
        self.professor = professor
        self.students: list[Student] = []

    def add_student(self, student: Student) -> int:
        if student in self.students:
            raise ValueError("Student is already enrolled in the course.")
        self.students.append(student)
        return len(self.students)

    def get_students(self) -> list:
        return [student.get_details() for student in self.students]

    def remove_student(self, student_id: str) -> int:
        for student in self.students:
            if student.get_details()[2] == student_id:
                self.students.remove(student)
                return len(self.students)
        raise ValueError("Student is not enrolled in the course.")

    def get_details(self) -> tuple:
        return self.course_code, self.course_name, self.professor.get_details(), len(self.students)
