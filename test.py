import unittest
from main import *

#check_input() tests
class TestInput(unittest.TestCase):
    def test_incorrect_input(self):
        out = check_input("string", "string", "string")
        self.assertEqual(out, 0)
    
    def test_correct_input(self):
        f, i, w = (check_input(5, 4, 100))
        self.assertEqual(f, 5)
        self.assertEqual(i, 4)
        self.assertEqual(w, 100)

#convert() tests
class TestConversion(unittest.TestCase):
    def test_valid_conversion(self):
        out = convert(5, 4)
        self.assertEqual(out, 64)
    
    def test_invalid_conversion(self):
        out = convert(5, 6)
        self.assertNotEqual(out, 65)

#calculate() tests
class TestCalculate(unittest.TestCase):
    def test_valid_calculate(self):
        out = calculate(64, 100)
        self.assertEqual(out, 17.6)
    
    def test_invalid_calculate(self):
        out = calculate(64, 105)
        self.assertNotEqual(out, 17.6)
        

#compare() tests
class TestCompareBoundary1(unittest.TestCase):
    def test_under_boundary1(self):
        out = compare(17.5)
        self.assertEqual(out, "underweight")
    
    def test_on_min_boundary1(self):
        out = compare(18.5)
        self.assertEqual(out, "normal weight")
    
    def test_inside_boundary1(self):
        out = compare(21)
        self.assertEqual(out, "normal weight")
        
    def test_on_max_boundary1(self):
        out = compare(25)
        self.assertEqual(out, "overweight")
        
    def test_over_boundary1(self):
        out = compare(26)
        self.assertEqual(out, "overweight")
        
class TestCompareBoundary2(unittest.TestCase):
    def test_under_boundary2(self):
        out = compare(24)
        self.assertEqual(out, "normal weight")
        
    def test_on_min_boundary2(self):
        out = compare(25)
        self.assertEqual(out, "overweight")
        
    def test_inside_boundary2(self):
        out = compare(27)
        self.assertEqual(out, "overweight")
        
    def test_on_max_boundary2(self):
        out = compare(30)
        self.assertEqual(out, "obese")
        
    def test_over_boundary2(self):
        out = compare(31)
        self.assertEqual(out, "obese")

unittest.main()