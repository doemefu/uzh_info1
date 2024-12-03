#!/usr/bin/python3

# Implement the following function according to the instruction.
def organize_employee_data(employees):
    return {outer[1]: {inner[0]: inner[2] for inner in employees if inner[1] == outer[1]} for outer in employees}

# The following lines call the function to print the return
# value to the Console. This way you can check what it does.
employees = [
    ('Alice', 'Engineering', 70000),
    ('Bob', 'HR', 50000),
    ('Charlie', 'Engineering', 80000),
    ('David', 'Sales', 45000),
    ('Eve', 'HR', 52000)
]
print(organize_employee_data(employees))
