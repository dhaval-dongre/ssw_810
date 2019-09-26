import unittest

def count_vowels(s):
    count=0
    s=s.lower()
    for x in range(0,len(s)):
        if s[x] in ['a','e','i','o','u']:
            count+=1
    
    return count

def last_occurrence(target, sequence):
    for pos, tar in enumerate(reversed(sequence)):
        if tar==target:
            return len(sequence)-1-pos
    
    raise ValueError("{} is not in the sequence".format(target))

def my_enumerate(seq):
    for i in len(seq):
        yield(i,seq)

class Fraction:
    def __init__(self, numerator, denominator):
        
        self.checkInput(numerator)
        self.checkInput(denominator)

        if denominator==0:
            raise ValueError("Denominator cannot be zero!")

        self.numerator=numerator
        self.denominator=denominator

        self.checkNegFraction(self.numerator,self.denominator)

        self.numerator=self.simplify().numerator
        self.denominator=self.simplify().denominator


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

    """ Ensures that the numerator and denominator are integers"""
    def checkInput(self, number):

        if(not isinstance(number,str) and not isinstance(number,int)):
            raise ValueError("Please ensure that the input is an integer!")

    def simplify(self):
        i = 1

        numerator=abs(self.numerator)
        denominator=abs(self.denominator)

        while(i <= numerator and i <= denominator):
            if(numerator % i == 0 and denominator % i == 0):
                gcd = i
                i =+ 1
        
        return Fraction(self.numerator/gcd, self.denominator/gcd)


