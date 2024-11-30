#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from car import Car

class CombustionCar(Car):

    def __init__(self, gas_capacity, gas_per_100km):
        if type(gas_capacity) != float or gas_capacity < 0:
            raise Warning("Bad input for gas_capacity")
        if type(gas_per_100km) != float or gas_per_100km < 0:
            raise Warning("Bad input for gas_per_100km")

        self.gas_capacity = gas_capacity
        self.gas_per_100km = gas_per_100km
        self.fuel_stat = gas_capacity

    def fuel(self, f):
        if type(f) != float or f < 0:
            raise Warning(f"Bad input for fuel: {f}")
        if self.fuel_stat + f > self.gas_capacity:
            raise Warning("Gas tank would be overfilled!")
        self.fuel_stat += f

    def get_gas_tank_status(self):
        return self.fuel_stat, self.gas_capacity

    def get_remaining_range(self):
        return self.fuel_stat / self.gas_per_100km * 100

    def drive(self, dist):
        if type(dist) != float or dist < 0:
            raise Warning("Bad input for dist")

        consumption = dist / 100 * self.gas_per_100km
        self.fuel_stat -= consumption
        if self.fuel_stat  <= 0:
            self.fuel_stat = 0
            raise Warning("Gas tank empty")