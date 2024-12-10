#!/usr/bin/env python3

from task.person import Person


class Student(Person):

    def __init__(self, name: str, email: str, student_id: str):
        super().__init__(name, email)
        self.student_id = student_id

    def get_details(self) -> tuple:
        return self.name, self.email, self.student_id
