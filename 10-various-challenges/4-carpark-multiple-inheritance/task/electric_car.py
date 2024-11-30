#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from car import Car

class ElectricCar(Car):

    def __init__(self, battery_size, battery_range_km):
        if type(battery_size) != float or battery_size < 0:
            raise Warning("Bad input for battery_size")
        if type(battery_range_km) != float or battery_range_km < 0:
            raise Warning("Bad input for battery_range_km")

        self.battery_size = battery_size
        self.battery_range_km = battery_range_km
        self.kwh_per_km = battery_size / battery_range_km
        self.battery_level = battery_size

    def charge(self, kwh):
        if type(kwh) != float or kwh < 0:
            raise Warning(f"Bad input for kwh: {kwh}")
        if self.battery_level + kwh > self.battery_size:
            raise Warning("Gas tank would be overfilled!")

        self.battery_level += kwh

    def get_battery_status(self):
        return self.battery_level, self.battery_size

    def get_remaining_range(self):
        return self.battery_level / self.kwh_per_km

    def drive(self, dist):
        if type(dist) != float or dist < 0:
            raise Warning("Bad input for dist")

        self.battery_level -= dist * self.kwh_per_km
        if self.battery_level  <= 0:
            self.battery_level = 0
            raise Warning("Battery empty")