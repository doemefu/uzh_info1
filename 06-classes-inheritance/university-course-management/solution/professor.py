#!/usr/bin/env python3

from task.person import Person


class Professor(Person):

    def __init__(self, name: str, email: str, employee_id: str, office: str):
        super().__init__(name, email)
        self.employee_id = employee_id
        self.office = office

    def get_details(self) -> tuple:
        return self.name, self.email, self.employee_id, self.office
