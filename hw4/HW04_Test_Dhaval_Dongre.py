import unittest
from HW04_Dhaval_Dongre import Fraction
from HW04_Dhaval_Dongre import count_vowels
from HW04_Dhaval_Dongre import last_occurrence
from HW04_Dhaval_Dongre import my_enumerate


class HW04Test(unittest.TestCase):

    def test_count_vowels(self):
        self.assertEqual(count_vowels('hello world'), 3)
        self.assertEqual(count_vowels('hEllO wrld'), 2)
        self.assertEqual(count_vowels('hll wrld'), 0)

    def test_last_occurence(self):
        self.assertEqual(last_occurrence('l','hello world'), 9)
        self.assertNotEqual(last_occurrence('l','hello world'), 19)

    def check_enumaration(self):
        self.assertTrue(list(my_enumerate('Hello!')) == list(enumerate('Hello!')), 'Expected both lists to be exact same')

    def check_fractions_equality(self):
        f1=Fraction(1,2)
        f2=Fraction(1,2)
        print(f"{f1} == {f2} is {f1==(f2)} [True]") 
        self.assertEqual(f1==(f2),True,f"{f1} == {f2} is {f1==(f2)} [True]")

        f1=Fraction(1,2)
        f2=Fraction(4,8)
        print(f"{f1} == {f2} is {f1==(f2)} [True]") 
        self.assertEqual(f1==(f2),True,f"{f1} == {f2} is {f1==(f2)} [True]")

        f1=Fraction(1,2)
        f2=Fraction(-4,8)
        print(f"{f1} == {f2} is {f1==(f2)} [True]") 
        self.assertNotEqual(f1==(f2),True,f"{f1} == {f2} is {f1==(f2)} [True]")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)