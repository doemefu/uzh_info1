#!/usr/bin/env python3

def get_bmi_category(height, weight):

    if height < 0 or weight < 0:
        return "N/A"

    bmi = weight / (height**2)

    if bmi < 0:
        return "N/A"
    elif bmi < 18.5:
        return f"BMI: {bmi:.2f}, Category: Underweight"
    elif bmi < 25:
        return f"BMI: {bmi:.2f}, Category: Normal weight"
    elif bmi < 30:
        return f"BMI: {bmi:.2f}, Category: Pre-obesity"
    elif bmi < 35:
        return f"BMI: {bmi:.2f}, Category: Obesity class I"
    elif bmi < 40:
        return f"BMI: {bmi:.2f}, Category: Obesity class II"
    else:
        return f"BMI: {bmi:.2f}, Category: Obesity class III"

#  call the function and print the return value to the Console
print(get_bmi_category(1.8, 70))
