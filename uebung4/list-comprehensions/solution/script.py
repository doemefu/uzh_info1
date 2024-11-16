#!/usr/bin/python3

def square_numbers(numbers):
    '''this one just serves as an example'''
    return [ number ** 2 for number in numbers ]

def even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def all_even(numbers):
    return [round(num) + 1 if round(num) % 2 != 0 else round(num) for num in numbers]

def only_integers(numbers):
    return [num for num in numbers if type(num) == type(1)]

def only_positive(numbers):
    return [abs(num) for num in numbers]

def from_1_to_1000_containing_a(a):
    return [num for num in range(1,1001) if str(a) in str(num)]

def multiple_of_a_and_greater_than_b(numbers, a, b):
    return [num for num in numbers if num % a == 0 and num > b]
