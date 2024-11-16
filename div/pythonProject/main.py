#!/usr/bin/env python3


# Calculate the tax.
# Change the functions below to calculate the right tax and return the amount.

# Standard tax rate is 8.1%
def standard_tax(amount):
    # You need to change the following part of the function
    # to calculate the right tax and return the correct amount.
    return amount * 0.081


# Reduced tax rate is 2.5%
def reduced_tax(amount):
    # You need to change the following part of the function
    # to calculate the right tax and return the correct amount.
    return amount * 0.025


# Accommodation tax rate is 3.7%
def accommodation_tax(amount):
    # You need to change the following part of the function
    # to calculate the right tax and return the correct amount.
    return amount * 0.037


# Helper function to round the tax to the nearest 0.05 increment.
def round_tax(tax):
    # You need to change the following part of the function
    # to round the tax to the nearest 0.05 increment and return it.
    return round(round(tax / 0.05) * 0.05, 2)


# Main function
def calculate_tax(amount, tax_type):
    # You need to change the following part of the function
    # to calculate the right tax and return the correct amount.
    if amount <= 0:
        return 0.0
    elif tax_type == standard_tax:
        return round_tax(standard_tax(amount))
    elif tax_type == reduced_tax:
        return round_tax(reduced_tax(amount))
    elif tax_type == accommodation_tax:
        return round_tax(accommodation_tax(amount))

    # Return the amount after you have calculated the tax.


# The following lines call the function and prints the return
# value to the Console. This way you can check what it does.
print(calculate_tax(101, standard_tax))
print(calculate_tax(101, reduced_tax))
print(calculate_tax(101, accommodation_tax))
