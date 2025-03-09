import unittest
import sys
import os

# Adjust the path to point to the 'main' directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../main')))

from assignment_3 import (
    euler_method,
    runge_kutta,
    function
)

class TestAssignment3(unittest.TestCase):

    def test_euler_method(self):
        # Test Euler's method for solving differential equations
        t0 = 0
        y0 = 1
        t_end = 2
        iterations = 10
        result = euler_method(function, t0, y0, t_end, iterations)
        self.assertAlmostEqual(result, 1.2446380979332121, places=5)  # Expected result

    def test_runge_kutta(self):
        # Test Runge-Kutta method for solving differential equations
        t0 = 0
        y0 = 1
        t_end = 2
        iterations = 10
        result = runge_kutta(function, t0, y0, t_end, iterations)
        self.assertAlmostEqual(result, 1.251316587879806, places=5)  # Expected result

    def test_function(self):
        # Test the differential equation function
        t = 1
        y = 1
        result = function(t, y)
        self.assertEqual(result, 0)  # f(1, 1) = 1 - 1^2 = 0

if __name__ == '__main__':
    unittest.main()