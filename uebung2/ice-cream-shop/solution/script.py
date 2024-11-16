#!/usr/bin/env python3

def get_price(price_cone,
        num_scoops_vanilla, price_per_scoop_vanilla,
        num_scoops_chocolate, price_per_scoop_chocolate):
    price = (price_cone + num_scoops_vanilla * price_per_scoop_vanilla + num_scoops_chocolate * price_per_scoop_chocolate)
    return price

