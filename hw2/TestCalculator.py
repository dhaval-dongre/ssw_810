
import unittest

from FractionCalculator import FractionCalculator

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestCalculator(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testEquals(self):
        f1=FractionCalculator(1,2)
        f2=FractionCalculator(1,2)
        print(f"{f1} == {f2} is {f1.equal(f2)} [True]") 
        self.assertEqual(f1.equal(f2),True,f"{f1} == {f2} is {f1.equal(f2)} [True]")
        # print(f"{f12} + {f12} = {f12.plus(f12)} [4/4]")

    def testAddition(self): 
        f1=FractionCalculator(1,2)
        f2=FractionCalculator(3,4)
        f3=f1.plus(f2)
        print(f"{f1} + {f2} is {f3} [10/8]") 
        self.assertEqual(str(f3),'10/8',f"{f1} + {f2} is {str(f3)} [10/8]")
        
    def testSubstraction(self): 
        f1=FractionCalculator(4,4)
        f2=FractionCalculator(1,2)
        f3=f1.minus(f2)
        print(f"{f1} - {f2} is {f3} [4/8]") 
        self.assertEqual(str(f3),"4/8",f"{f1} - {f2} is {f3} [4/8]")

    def testMultiplication(self): 
        f1=FractionCalculator(1,2)
        f2=FractionCalculator(1,2)
        f3=f1.times(f2)
        print(f"{f1} * {f2} is {f3} [1/4]") 
        self.assertEqual(str(f3),"1/4",f"{f1} * {f2} is {f3} [1/4]")

    def testDivision(self): 
        f1=FractionCalculator(4,4)
        f2=FractionCalculator(1,2)
        f3=f1.divide(f2)
        print(f"{f1} / {f2} is {f3} [8/4]") 
        self.assertEqual(str(f3),"8/4",f"{f1} / {f2} is {f3} [8/4]")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

