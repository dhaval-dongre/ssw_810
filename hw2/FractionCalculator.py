from fractions import Fraction

class FractionCalculator:
    def __init__(self, numerator, denominator):

        if(not isinstance(numerator,str) and not isinstance(numerator,int)):
            raise ValueError("Please ensure that the input is an integer!")
        
        try:
            self.numerator=int(numerator)
            self.denominator=int(denominator)

        except ValueError:
            raise ValueError("Please ensure that the input is an integer!")

        if self.denominator==0:
            raise ValueError("Denominator cannot be zero!")
        

    def __str__(self):
        return str(self.numerator)+"/"+str(self.denominator)

    def equal(self,other):
        if self.numerator*other.denominator==self.denominator*other.numerator:
            return True
        else:
            return False

    def plus(self,other):
        denom=self.denominator*other.denominator
        num=self.numerator*other.denominator+other.numerator*self.denominator
        return FractionCalculator(num,denom)
    
    def minus(self,other):
        denom=self.denominator*other.denominator
        num=self.numerator*other.denominator-other.numerator*self.denominator
        return FractionCalculator(num,denom)

    def times(self, other):
        denom=self.denominator*other.denominator
        num=self.numerator*other.numerator
        return FractionCalculator(num,denom)

    def divide(self,other):
        denom=self.denominator*other.numerator
        num=self.numerator*other.denominator
        return FractionCalculator(num,denom)

    @staticmethod
    def main():
        print("Welcome to the fraction calculator!")

        num1=input("Fraction 1 numerator:")
        denom1=input("Fraction 1 denominator:")
        num2=input("Fraction 2 numerator:")
        denom2=input("Fraction 2 denominator:")

        fraction1= FractionCalculator(num1,denom1)
        fraction2= FractionCalculator(num2,denom2)

        operator=input("Operation (+, -, *, /, ==):")

        if(operator not in ['+','-','*','/','==']):
            raise ValueError("Invalid Operator!")
        
        elif operator=='==':
            print(fraction1.equal(fraction2))

        elif operator=='+':
            print(fraction1.plus(fraction2))
        
        elif operator=='-':
            print(fraction1.minus(fraction2))

        elif operator=='*':
            print(fraction1.times(fraction2))

        elif operator=='/':
            print(fraction1.divide(fraction2))

if __name__=="__main__":
    FractionCalculator.main()    