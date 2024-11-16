#!/usr/bin/env python3

# Height in M
height = 10
# Weight in KG
weight = 10


# Determine the BMI. Change the function
# below to calculate the BMI return which category the result is in.
# Your implementation should work with any specific value.
# You must use the variables defined above.


def get_bmi_category():

    if height < 0 or weight < 0:
        return "N/A"

    bmiValue = weight / height**2

    if bmiValue <= 18.5:
        cat = "Underweight"
    elif 18.5 < bmiValue <= 25:
        cat = "Normal weight"
    elif 25 < bmiValue <= 30:
        cat = "Pre-obesity"
    elif 30 < bmiValue <= 35:
        cat = "Obesity class I"
    elif 35 < bmiValue <= 40:
        cat = "Obesity class II"
    else:
        cat = "Obesity class III"
    
    return f"BMI: {bmiValue:.2f}, Category: {cat}"

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(get_bmi_category())
