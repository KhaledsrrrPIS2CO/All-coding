import unittest
from circle_area import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def Test_area(self):
        #Test area when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2,1), pi *(2.1**2))
        
