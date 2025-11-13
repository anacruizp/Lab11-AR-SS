#https://github.com/anacruizp/Lab11-AR-SS.git
#Partner 1: Ana Ruiz
#Partner 2: Sandra Salkini
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(-2,3), 1)
        self.assertEqual(add(0,5), 5)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5,2),3)
        self.assertEqual(subtract(2,5),-3)
        self.assertEqual(subtract(-3,-6),3)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(10,2),5)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(5,0)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(100, 10), 2)
        self.assertAlmostEqual(logarithm(8, 2), 3)
        self.assertAlmostEqual(logarithm(1, 10), 0)


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, 1)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(5, 0)
        with self.assertRaises(ValueError):
            logarithm(10,1)
        with self.assertRaises(ValueError):
            logarithm(-8,2)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3,4), 5.0)
        self.assertAlmostEqual(hypotenuse(0,0),0.0)
        self.assertAlmostEqual(hypotenuse(-3,-4),5.0)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(9),3)
        self.assertAlmostEqual(square_root(2.25),1.5)
        with self.assertRaises(ValueError):
            square_root(-4)

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
