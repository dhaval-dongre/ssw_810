
import unittest

from FractionCalculator import FractionCalculator

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestCalculator(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testEquals(self):
        f1=FractionCalculator(1,2)
        f2=FractionCalculator(1,2) 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testAddition(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testSubstraction(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testMultiplication(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testDivision(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

