#!/usr/bin/env python3

from unittest import TestCase
from combustion_car import CombustionCar
from electric_car import ElectricCar
from hybrid_car import HybridCar


class TestCars(TestCase):

    def test_comb_type_0(self):
        with self.assertRaises(Warning):
            c = CombustionCar(40.0, "a")

    def test_comb_type_1(self):
        with self.assertRaises(Warning):
            c = CombustionCar("a", 1.0)

    def test_comb_type_2(self):
        with self.assertRaises(Warning):
            c = CombustionCar(-1.0, 1.0)

    def test_comb_type_4(self):
        with self.assertRaises(Warning):
            c = CombustionCar(1.0, -1.0)

    def test_comb_type_5(self):
        c = CombustionCar(40.0, 8.0)
        with self.assertRaises(Warning):
            c.drive(-1.0)

    def test_comb_type_6(self):
        c = CombustionCar(40.0, 8.0)
        with self.assertRaises(Warning):
            c.drive("a")

    def test_comb_type_7(self):
        c = CombustionCar(40.0, 8.0)
        with self.assertRaises(Warning):
            c.drive(-1.0)

    def test_comb_remaining_range(self):
        c = CombustionCar(40.0, 8.0)
        self.assertAlmostEqual(500.0, c.get_remaining_range(), delta=0.001)

    def test_comb_drive(self):
        c = CombustionCar(40.0, 8.0)
        c.drive(25.0)
        self.assertAlmostEqual(38.0, c.get_gas_tank_status()[0], delta=0.001)

    def test_comb_fuel(self):
        c = CombustionCar(40.0, 8.0)
        c.drive(25.0)
        c.fuel(1.0)
        self.assertAlmostEqual(39.0, c.get_gas_tank_status()[0], delta=0.001)

    def test_comb_drive_empty(self):
        c = CombustionCar(40.0, 8.0)
        with self.assertRaises(Warning):
            c.drive(1000.0)

    def test_comb_get_gas_tank_status(self):
        c = CombustionCar(40.0, 8.0)
        self.assertAlmostEqual(40.0, c.get_gas_tank_status()[0], delta=0.001)

#------------------------------------------------------------------------

# class TestElectricCars(TestCase): #Optional to only run Electric tests

    def test_electric_type_0(self):
        with self.assertRaises(Warning):
            e = ElectricCar(40.0, "a")

    def test_electric_type_1(self):
        with self.assertRaises(Warning):
            e = ElectricCar("a", 1.0)

    def test_electric_type_2(self):
        with self.assertRaises(Warning):
            e = ElectricCar(-1.0, 1.0)

    def test_electric_type_4(self):
        with self.assertRaises(Warning):
            e = ElectricCar(1.0, -1.0)

    def test_electric_type_5(self):
        e = ElectricCar(40.0, 8.0)
        with self.assertRaises(Warning):
            e.drive(-1.0)

    def test_electric_type_6(self):
        e = ElectricCar(40.0, 8.0)
        with self.assertRaises(Warning):
            e.drive("a")

    def test_electric_type_7(self):
        e = ElectricCar(40.0, 8.0)
        with self.assertRaises(Warning):
            e.drive(-1.0)

    def test_electric_remaining_range(self):
        e = ElectricCar(25.0, 500.0)
        self.assertAlmostEqual(500.0, e.get_remaining_range(), delta=0.001)

    def test_electric_get_battery_status(self):
        e = ElectricCar(25.0, 500.0)
        self.assertAlmostEqual(25.0, e.get_battery_status()[0], delta=0.001)

    def test_electric_drive(self):
        e = ElectricCar(25.0, 500.0)
        e.drive(100.0)
        self.assertAlmostEqual(20.0, e.get_battery_status()[0], delta=0.001)

    def test_electric_charge(self):
        e = ElectricCar(25.0, 500.0)
        e.drive(100.0)
        e.charge(2.0)
        self.assertAlmostEqual(22.0, e.get_battery_status()[0], delta=0.001)

    def test_electric_drive_empty(self):
        e = ElectricCar(25.0, 500.0)
        with self.assertRaises(Warning):
            e.drive(1000.0)

#------------------------------------------------------------------------

# class TestHybridCars(TestCase): #Optional to only run hybrid tests

    def test_hybrid_remaining_range_electric(self):
        h = HybridCar(40.0, 8.0, 25.0, 400.0)
        self.assertAlmostEqual(900.0, h.get_remaining_range(), delta=0.001)

    def test_hybrid_remaining_range_electric_2(self):
        h = HybridCar(40.0, 8.0, 25.0, 1.0)
        self.assertAlmostEqual(501.0, h.get_remaining_range(), delta=0.001)

    def test_hybrid_remaining_range_combustion(self):
        h = HybridCar(40.0, 8.0, 25.0, 400.0)
        h.switch_to_combustion()
        self.assertAlmostEqual(900, h.get_remaining_range(), delta=0.001)

    def test_hybrid_drive_combustion_empty(self):
        h = HybridCar(40.0, 8.0, 25.0, 400.0)
        h.switch_to_combustion()
        h.drive(600.0)
        self.assertEqual("electric", h.mode)

    def test_hybrid_drive_combustion_empty_2(self):
        h = HybridCar(40.0, 8.0, 25.0, 400.0)
        h.switch_to_combustion()
        h.drive(600.0)
        self.assertAlmostEqual(0.0, h.get_gas_tank_status()[0], delta=0.001)

    def test_hybrid_drive_combustion_empty_3(self):
        h = HybridCar(40.0, 8.0, 25.0, 500.0)
        h.switch_to_combustion()
        h.drive(600.0)
        self.assertAlmostEqual(20.0, h.get_battery_status()[0], delta=0.001)



    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
