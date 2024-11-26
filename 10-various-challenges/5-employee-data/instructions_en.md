# **Organizing Employee Data**
This task focuses on improving skills in dictionary comprehensions by implementing a function that organizes employee data into a structured nested dictionary. You are provided with a list of employee records, where each record contains the employee’s name, department, and salary.

In `script.py`, you are provided with a partially implemented function `organize_employee_data(employees)`. Your task is to complete this function using a dictionary comprehension that returns a nested dictionary organizing employees by their departments.

**Input Format:**  
The input is a list of tuples, where each tuple consists of three elements: `(name, department, salary)`. For example:
```
[
    ('Alice', 'Engineering', 70000),
    ('Bob', 'HR', 50000),
    ('Charlie', 'Engineering', 80000),
    ('David', 'Sales', 45000),
    ('Eve', 'HR', 52000)
]
```

**Output Format:**
The output should be a nested dictionary where each key is a department name, and its value is another dictionary mapping employee names to their salaries. For example:

```
{
    'Engineering': {'Alice': 70000, 'Charlie': 80000},
    'HR': {'Bob': 50000, 'Eve': 52000},
    'Sales': {'David': 45000}
}
```

**Note:** Implement the entire solution using dictionary comprehensions, potentially using nested comprehensions.
The function must start with a `return` statement containing the dictionary comprehension.

**Note:** Ensure that each department appears only once as a key in the outer dictionary.
Employee names within each department should be unique, with the latest salary overwriting any previous entries if duplicates exist.

**Note:** Make sure that your solution is self-contained within the `organize_employee_data(employees)` function.
You may test your solution with different inputs, but do not change the name of the main function or the automated grading will fail.
