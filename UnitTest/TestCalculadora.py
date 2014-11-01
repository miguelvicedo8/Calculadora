#!/usr/bin/python
# -*- coding: utf8 -*-


import unittest
import sys
sys.path.append('../')
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_suma_2_mas_2(self):
        cal = Calculator()
        self.assertEqual(4, cal.suma(2, 2))

    def test_suma_3_mas_2(self):
        cal = Calculator()
        self.assertEqual(5, cal.suma(3, 2))

    def test_suma_5_mas_3(self):
        cal = Calculator()
        self.assertEqual(8, cal.suma(5, 3))

    def test_resta_5_menos_3(self):
        cal = Calculator()
        self.assertEqual(2, cal.resta(5, 3))

    def test_resta_5_menos_1(self):
        cal = Calculator()
        self.assertEqual(4, cal.resta(5, 1))

    def test_resta_10_menos_2(self):
        cal = Calculator()
        self.assertEqual(8, cal.resta(10, 2))

    def test_multiplica_5_por_3(self):
        cal = Calculator()
        self.assertEqual(15, cal.multiplica(5, 3))

    def test_multiplica_5_por_1(self):
        cal = Calculator()
        self.assertEqual(5, cal.multiplica(5, 1))

    def test_multiplica_10_por_2(self):
        cal = Calculator()
        self.assertEqual(20, cal.multiplica(10, 2))

    def test_divide_6_entre_3(self):
        cal = Calculator()
        self.assertEqual(2, cal.divide(6, 3))

    def test_divide_5_entre_1(self):
        cal = Calculator()
        self.assertEqual(5, cal.divide(5, 1))

    def test_divide_10_entre_2(self):
        cal = Calculator()
        self.assertEqual(5, cal.divide(10, 2))

if __name__ == "__main__":
    unittest.main()
