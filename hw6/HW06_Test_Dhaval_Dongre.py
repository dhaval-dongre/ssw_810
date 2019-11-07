import unittest
from HW06_Dhaval_Dongre import *

class TestList(unittest.TestCase):
    
    def test_list_copy(self):
       """verifies whether the copy of the list is the same as the original"""
       self.assertEqual([1,2,3],list_copy([1,2,3]))
       self.assertNotEqual([1,2,2,3],list_copy([1,2,3]))

    def test_list_intersect(self):
        """verifies whether the common elements between 2 lists is as expected in a list format"""
        self.assertEqual(list_intersect([1,2,3],[1,2]),[1,2])

    def test_list_difference(self):
        """verifies whether the difference between 2 lists is as expected in a list format"""
        self.assertEqual(list_difference([1,2,3],[1,2]),[3])
        self.assertEqual(list_difference([1,2,3,2],[1,2]),[3])

    def test_remove_vowels(self):
        """verifies whether the vowels are removed as expected by the remove_vowels function"""
        self.assertEqual(remove_vowels('aeiou'),'')
        self.assertEqual(remove_vowels('Laeiouau'),'L')

    def test_check_pwd(self):
        """verifies whether the password matches our criteria of uppercase, lowercase and digit"""
        self.assertEqual(check_pwd('Dh@v@l4'),True)
        self.assertEqual(check_pwd('Dhaval'),False)

    def test_insertion_sort(self):
        """verifies our insertion sort logic and confirms whether the list is sorted as expected"""
        self.assertEqual(insertion_sort([8,2,1,3,5,5,4]),[1, 2, 3, 4, 5, 5, 8])

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)