import unittest

 # checks the number of vowels in a given string

def count_vowels(s):
    count=0
    s=s.lower()
    for x in range(0,len(s)):
        if s[x] in ['a','e','i','o','u']:
            count+=1
    
    return count

""" finds the last occurence of an element in a given sequence"""
def last_occurrence(target, sequence):
    for pos, tar in enumerate(reversed(sequence)):
        if tar==target:
            return len(sequence)-1-pos
    
    raise ValueError("{} is not in the sequence".format(target))

""" a generator function which returns each element in a sequence"""
def my_enumerate(seq):
    for i in range(len(seq)):
        yield(i,seq[i])

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
        frac1=self.simplify()
        frac2=other.simplify()

        if frac1.numerator*frac2.denominator==frac1.denominator*frac2.numerator:
            return True
        else:
            return False

    """ Ensures that the numerator and denominator are integers"""
    def checkInput(self, number):

        if(not isinstance(number,str) and not isinstance(number,int)):
            raise ValueError("Please ensure that the input is an integer!")

    """ simplifies a fraction which can be reduced"""
    def simplify(self):
        i = 1

        numerator=abs(self.numerator)
        denominator=abs(self.denominator)

        while(i <= numerator and i <= denominator):
            if(numerator % i == 0 and denominator % i == 0):
                gcd = i
            i =i+ 1
        

        return Fraction(int(self.numerator/gcd), int(self.denominator/gcd))


