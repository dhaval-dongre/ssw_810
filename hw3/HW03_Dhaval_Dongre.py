import unittest

"""Solely responsible for performing all mathematical and logical opeartions on fractions"""
class Fraction:
    def __init__(self, numerator, denominator):
        
        self.checkInput(numerator)
        self.checkInput(denominator)

        if denominator==0:
            raise ValueError("Denominator cannot be zero!")

        self.numerator=numerator
        self.denominator=denominator

        self.checkNegFraction(self.numerator,self.denominator)

    """Returns the fraction in string format"""
    def __str__(self):
        return str(self.numerator)+"/"+str(self.denominator)

    """rectifies the -ve val in the fraction"""
    def checkNegFraction(self, numerator, denominator):
        if denominator<0:
            self.numerator=numerator*-1
            self.denominator=denominator*-1

    """Checks whether two fractions are equal or not"""
    def __eq__(self,other):
        if self.numerator*other.denominator==self.denominator*other.numerator:
            return True
        else:
            return False

    """Adds two fractions and returns the result"""
    def __add__(self,other):
        denom=self.denominator*other.denominator
        num=self.numerator*other.denominator+other.numerator*self.denominator
        return Fraction(num,denom)
    
    """Subtracts two fractions and returns the result"""
    def __sub__(self,other):
        denom=self.denominator*other.denominator
        num=self.numerator*other.denominator-other.numerator*self.denominator
        return Fraction(num,denom)

    """Multiplies two fractions and returns the result"""
    def __mul__(self, other):
        denom=self.denominator*other.denominator
        num=self.numerator*other.numerator
        return Fraction(num,denom)

    """Divides two fractions and returns the result"""
    def __truediv__(self,other):
        denom=self.denominator*other.numerator
        num=self.numerator*other.denominator
        return Fraction(num,denom)

    """ Ensures that the numerator and denominator are integers"""
    def checkInput(self, number):

        if(not isinstance(number,str) and not isinstance(number,int)):
            raise ValueError("Please ensure that the input is an integer!")


    """ checks whether 2 fractions are unequal or not"""
    def __ne__(self, other): 
        return self.numerator/self.denominator!=(other.numerator/other.denominator)

    """ checks whether the first fraction is less than the second"""
    def __lt__(self, other): #less than
        return self.numerator/self.denominator<(other.numerator/other.denominator)

    """ checks whether the first fraction is less than or equal to the second"""
    def __le__(self, other): #less than or equal to
        return self.numerator/self.denominator<=(other.numerator/other.denominator)

    """ checks whether the first fraction is greater than the second"""
    def __gt__(self, other): #greater than
        return self.numerator/self.denominator>(other.numerator/other.denominator)

    """ checks whether the first fraction is greater than or equal to the second"""
    def __ge__(self, other): #greater than or equal to
        return self.numerator/self.denominator>=(other.numerator/other.denominator)


"""Class containing unittests which validates all the mathematical and logical operations defined in the Fraction class"""
class TestFraction(unittest.TestCase):

    """ Unit test for validating equality of two fractions"""
    def testEquals(self):
        f1=Fraction(1,2)
        f2=Fraction(1,2)
        print(f"{f1} == {f2} is {f1==(f2)} [True]") 
        self.assertEqual(f1==(f2),True,f"{f1} == {f2} is {f1==(f2)} [True]")
        # print(f"{f12} + {f12} = {f12.plus(f12)} [4/4]")

    """ Unit test for validating addition of two fractions"""
    def testAddition(self): 
        f1=Fraction(1,2)
        f2=Fraction(3,4)
        f3=f1+f2
        print(f"{f1} + {f2} is {f3} [10/8]") 
        self.assertEqual(str(f3),'10/8',f"{f1} + {f2} is {str(f3)} [10/8]")
        
        f1=Fraction(1,2)
        f2=Fraction(3,4)
        f3=f1+f2
        print(f"{f1} + {f2} is {f3} [10/8] not [-1/2]") 
        self.assertNotEqual(str(f3),'-1/2',f"{f1} + {f2} is {str(f3)} not [-1/2]")

    """ Unit test for validating subtraction of two fractions"""
    def testSubstraction(self): 
        f1=Fraction(4,4)
        f2=Fraction(1,2)
        f3=f1-f2
        print(f"{f1} - {f2} is {f3} [4/8]") 
        self.assertEqual(str(f3),"4/8",f"{f1} - {f2} is {f3} [4/8]")

        f1=Fraction(4,4)
        f2=Fraction(1,2)
        f3=f1-f2
        print(f"{f1} - {f2} is {f3} [4/8]") 
        self.assertNotEqual(str(f3),"2/8",f"{f1} - {f2} is {f3} [4/8] not [2/8]")
    
    """ Unit test for validating multiplication of two fractions"""
    def testMultiplication(self): 
        f1=Fraction(1,2)
        f2=Fraction(1,2)
        f3=f1*f2
        print(f"{f1} * {f2} is {f3} [1/4]") 
        self.assertEqual(str(f3),"1/4",f"{f1} * {f2} is {f3} [1/4]")

    """ Unit test for validating division of two fractions"""
    def testDivision(self): 
        f1=Fraction(4,4)
        f2=Fraction(1,2)
        f3=f1/f2
        print(f"{f1} / {f2} is {f3} [8/4]") 
        self.assertEqual(str(f3),"8/4",f"{f1} / {f2} is {f3} [8/4]")

    """ Unit test for validating inequality of two fractions"""
    def testInequality(self):
        f1=Fraction(1,2)
        f2=Fraction(1,3)
        print(f"{f1} != {f2} is {f1!=(f2)} [True]") 
        self.assertEqual(f1!=(f2),True,f"{f1} != {f2} is {f1!=(f2)} [True]")

    """ Unit test for validating whether the first fraction is less than the second"""
    def testLessThan(self):
        f1=Fraction(1,3)
        f2=Fraction(1,2)
        print(f"{f1} < {f2} is {f1<(f2)} [True]") 
        self.assertEqual(f1<(f2),True,f"{f1} < {f2} is {f1<(f2)} [True]")

    """ Unit test for validating whether the first fraction is less than or equal to the second"""
    def testLessThanEqual(self):
        f1=Fraction(1,3)
        f2=Fraction(1,2)
        print(f"{f1} <= {f2} is {f1<=(f2)} [True]") 
        self.assertEqual(f1<=(f2),True,f"{f1} <= {f2} is {f1<=(f2)} [True]")

        f1=Fraction(1,2)
        f2=Fraction(1,2)
        print(f"\t\t\t\t{f1} <= {f2} is {f1<=(f2)} [True]") 
        self.assertEqual(f1<=(f2),True,f"{f1} <= {f2} is {f1<=(f2)} [True]")

    """ Unit test for validating whether the first fraction is greater than the second"""
    def testGreaterThan(self):
        f1=Fraction(1,2)
        f2=Fraction(1,3)
        print(f"\t\t\t\t{f1} > {f2} is {f1>(f2)} [True]") 
        self.assertEqual(f1>(f2),True,f"{f1} > {f2} is {f1>(f2)} [True]")

        f1=Fraction(1,2)
        f2=Fraction(1,3)
        print(f"\t\t\t\t{f1} > {f2} is {f1>(f2)} [True]") 
        self.assertNotEqual(f1>(f2),False,f"{f1} > {f2} is {f1>(f2)} [True] not [False]")

    """ Unit test for validating whether the first fraction is greater than or equal to the second"""
    def testGreaterThanEqual(self):
        f1=Fraction(1,2)
        f2=Fraction(1,3)
        print(f"{f1} >= {f2} is {f1>=(f2)} [True]") 
        self.assertEqual(f1>=(f2),True,f"{f1} >= {f2} is {f1>=(f2)} [True]")

        f1=Fraction(1,2)
        f2=Fraction(1,2)
        print(f"\t\t\t\t{f1} >= {f2} is {f1>=(f2)} [True]") 
        self.assertEqual(f1>=(f2),True,f"{f1} >= {f2} is {f1>=(f2)} [True]")

    def testNotEquals(self):
        f1=Fraction(1,2)
        f2=Fraction(1,-2)
        print(f"{f1} == {f2} is {f1==(f2)} [True]") 
        self.assertNotEqual(f1==(f2),True,f"{f1} == {f2} is {f1==(f2)} [False]")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
