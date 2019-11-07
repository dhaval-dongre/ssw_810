import unittest
from HW07_Dhaval_Dongre import anagram_lst, anagrams_cntr, anagrams_dd, covers_alphabet, book_index


class TestContainer(unittest.TestCase):

    def test_anagram_lst(self):
        """verifies whether the anagram_lst() method correctly identifies anagrams"""
        self.assertEqual(anagram_lst('dormitory', 'Dirty roomss'), False)
        self.assertTrue(anagram_lst('dormitory', 'dirtyroom'))
        self.assertTrue(anagram_lst('', ''))

    def test_anagrams_dd(self):
        """verifies whether the anagrams_dd() method correctly identifies anagrams"""
        self.assertEqual(anagram_lst('dormitory', 'Dirty roomss'), False)
        self.assertTrue(anagram_lst('dormitory', 'dirtyroom'))
        self.assertTrue(anagram_lst('', ''))

    def test_anagrams_cntr(self):
        """verifies whether the anagrams_cntr() method correctly identifies anagrams"""
        self.assertEqual(anagram_lst('dormitory', 'Dirty roomss'), False)
        self.assertTrue(anagram_lst('dormitory', 'dirtyroom'))
        self.assertTrue(anagram_lst('', ''))

    def test_covers_alphabet(self):
        """verifies whether the covers_aplhabet() method correctly identifies that the given string
        has all the alphabets """
        self.assertEqual(covers_alphabet('AbCdefghiJklomnopqrStuvwxyz'), True)
        self.assertTrue(covers_alphabet(
            "We promptly judged antique ivory buckles for the next prize"))
        self.assertFalse(covers_alphabet("xyz"))

    def test_book_index(self):
        """verifies whether the booh_index() method correctly returns all the occurences of words along
        with the page number in a list format"""

        woodchucks = [('how', 3), ('much', 3), ('wood', 3), ('would', 2), ('a', 1), ('woodchuck', 1),
                      ('chuck', 3), ('if', 1), ('a', 1), ('woodchuck', 2), ('could', 2), ('chuck', 1), ('wood', 1)]
        list = [
            [
                'a', [1]], [
                'chuck', [
                    1, 3]], [
                    'could', [2]], [
                        'how', [3]], [
                            'if', [1]], [
                                'much', [3]], [
                                    'wood', [
                                        1, 3]], [
                                            'woodchuck', [
                                                1, 2]], [
                                                    'would', [2]]]

        self.assertEqual(book_index(woodchucks), list)
        self.assertEqual(book_index([('word1', 1), ('word2', 2), ('word1', 1), ('word1', 3)]), [
                         ['word1', [1, 3]], ['word2', [2]]])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
