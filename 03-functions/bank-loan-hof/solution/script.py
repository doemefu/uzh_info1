#!/usr/bin/env python3

def lump_sum(principal, interest_rate, number_periods):
    return principal * interest_rate * number_periods + principal

def annuity(principal, interest_rate, number_periods):
    annuity_payment = (principal * interest_rate) / (1 - (1 + interest_rate)**(-number_periods))
    return annuity_payment * number_periods

def total_sum_repaid(payment_type):
    if payment_type == "annuity":
        return annuity
    elif payment_type == "lump_sum":
        return lump_sum
    else:
        return 'Invalid payment type. Allowed payment types are: annuity or lump_sum!'

# The following lines call the function and prints the return
# value to the console. This way you can check what it does.
print(total_sum_repaid("annuity")(10000, 0.01, 10))
print(total_sum_repaid("lump_sum")(10000, 0.01, 10))
