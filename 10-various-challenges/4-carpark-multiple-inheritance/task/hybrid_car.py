#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from combustion_car import CombustionCar
from electric_car import ElectricCar

class HybridCar(CombustionCar, ElectricCar):

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        CombustionCar.__init__(self,gas_capacity, gas_per_100km)
        ElectricCar.__init__(self,battery_size,battery_range_km)
        self.mode = "electric"

    def switch_to_combustion(self):
        self.mode = "combustion"

    def switch_to_electric(self):
        self.mode = "electric"

    def get_remaining_range(self):
        if self.mode == "electric":
            return ElectricCar.get_remaining_range(self)
        else:
            return CombustionCar.get_remaining_range(self)

    def drive(self, dist):
        delta = dist - self.get_remaining_range()
        if self.mode == "electric":
            try:
                ElectricCar.drive(self, dist)
            except Warning:
                self.switch_to_combustion()
                CombustionCar.drive(self,delta)
        else:
            try:
                CombustionCar.drive(self, dist)
            except Warning:
                self.switch_to_electric()
                ElectricCar.drive(self, delta)