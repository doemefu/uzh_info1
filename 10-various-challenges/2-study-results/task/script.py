#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def get_average_grade(path):
    if not os.path.exists(path):
        return None

    with open(path, "r") as fi:
        content = fi.read()

        grades = []

        for line in content.splitlines():
            if len(line) == 0 or line[0] == "#":
                continue
            else:
                grade = line.split(":")

                grades.append(float(grade[1]))

    return round(sum(grades)/len(grades),2) if len(grades) != 0 else 0.0

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(get_average_grade("./my_grades.txt"))

