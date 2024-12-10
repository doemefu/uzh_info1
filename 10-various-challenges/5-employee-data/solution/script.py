#!/usr/bin/python3

def organize_employee_data(employees):
    return {
        dept: {name: salary for name, department, salary in employees if department == dept}
        for dept in set(department for _, department, _ in employees)
    }
