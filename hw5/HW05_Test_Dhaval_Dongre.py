import unittest
from HW05_Dhaval_Dongre import *

class TestString(unittest.TestCase):
    
    def test_reverse(self):
       """verifies whether the reverse functions reverses the given string as expected"""
       self.assertEqual(reverse('abc'),'cba')
       self.assertNotEqual(reverse('abc'),'abc')
       self.assertEqual(reverse('abbabba'),'abbabba')

    def test_rev_enumerate(self):
        """verifies whether the custom generator function is enumerating the offset and each element in a reverse order"""
        revList=list(enumerate('abc'))
        revList.reverse()
        self.assertEqual(list(rev_enumerate('abc')),revList)
        self.assertNotEqual(list(rev_enumerate('abc')),list(enumerate('abc')))

    def test_find_second(self):
        """verifies the second occurence of the target is as expected in the given string"""
        self.assertEqual(find_second('a','babac'),3)
        self.assertEqual(find_second('ab','abab'),2)
        self.assertEqual(find_second('abba', 'abbabba'),3)

    def test_get_lines(self):
        """verifies the get_lines function as per our set requirements"""
        file_name = 'C:/Users/Dhaval/Documents/ssw_810/hw5/test.txt'

        expected = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>','<line4.1 line4.2>', '<line5>', '<line6>']
        result = list(get_lines(file_name))
        self.assertEqual(result, expected)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)