#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from combustion_car import CombustionCar
from electric_car import ElectricCar

class HybridCar(CombustionCar, ElectricCar):

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        if type(battery_size) != float or battery_size < 0:
            raise Warning("Bad input for battery_size")
        if type(battery_range_km) != float or battery_range_km < 0:
            raise Warning("Bad input for battery_range_km")
        if type(gas_capacity) != float or gas_capacity < 0:
            raise Warning("Bad input for gas_capacity")
        if type(gas_per_100km) != float or gas_per_100km < 0:
            raise Warning("Bad input for gas_per_100km")

        CombustionCar.__init__(self,gas_capacity, gas_per_100km)
        ElectricCar.__init__(self,battery_size,battery_range_km)
        self.mode = "electric"

    def switch_to_combustion(self):
        self.mode = "combustion"

    def switch_to_electric(self):
        self.mode = "electric"

    def get_remaining_range(self):
        print(ElectricCar.get_remaining_range(self))
        return ElectricCar.get_remaining_range(self) + CombustionCar.get_remaining_range(self)

    def drive(self, dist):
        if type(dist) != float or dist < 0:
            raise Warning("Bad input for dist")

        if self.mode == "electric":
            delta = dist -  ElectricCar.get_remaining_range(self)
            try:
                ElectricCar.drive(self, dist)
            except Warning:
                self.switch_to_combustion()
                CombustionCar.drive(self,delta)
        else:
            delta = dist -  CombustionCar.get_remaining_range(self)
            try:
                CombustionCar.drive(self, dist)
            except Warning:
                self.switch_to_electric()
                ElectricCar.drive(self, delta)