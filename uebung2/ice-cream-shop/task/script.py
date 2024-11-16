#!/usr/bin/env python3

# Change the function below to calculate the total price this
# order. Note that your implementation should work with any
# specific value, so you can't just add up the raw numbers,
# you MUST use the variables passed as parameters.
def get_price(price_cone,
        num_scoops_vanilla, price_per_scoop_vanilla,
        num_scoops_chocolate, price_per_scoop_chocolate):
    # Modify this return statement so that the correct result is returned    
    return price_cone + (num_scoops_chocolate * price_per_scoop_chocolate) + (num_scoops_vanilla * price_per_scoop_vanilla)


# The following line calls the function and prints its return value. You don't
# need to change it, it's only here so you can see the result in the "Console
# Output" tab below. You can try entering different values to ensure your
# implementation works correctly.
print(get_price(0.50, 1, 1.20, 2, 1.20))
