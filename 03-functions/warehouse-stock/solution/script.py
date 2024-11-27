#!/usr/bin/python3

def add_stock(warehouse, product):
    if product not in warehouse:
        warehouse[product] = 0
    warehouse[product] += 1

def remove_stock(warehouse, product):
    if product not in warehouse:
        print(f"{product} not in stock")
    elif warehouse[product] == 1:
        del(warehouse[product])
    else:
        warehouse[product] -= 1

def get_stock(warehouse, product):
    if product not in warehouse:
        return 0
    else:
        return warehouse[product]

