import unittest
from HW10_Dhaval_Dongre import Repository


class TestRepository(unittest.TestCase):

    def test_pretty_print_Student(self):
        """checks whether the content of the dictionary generated by the Student class is as expected"""
        fa = Repository('C:/Users/Dhaval/Documents/ssw_810/hw10/test')
        d = {
            '10103': [
                'Baldwin, C', 'SFEN',
                'CS 501',
                'SSW 564',
                'SSW 567',
                'SSW 687'],
            '10115': [
                'Wyatt, X', 'SFEN',
                'SSW 564',
                'SSW 567']}

        self.assertDictEqual(fa.student.summary, d)

        with self.assertRaises(FileNotFoundError):
            Repository('C:/Users/Dhaval/Documents/ssw_810/hw10/blablabla')

        fa.student.pretty_print()

    def test_pretty_print_Instructor(self):
        """checks whether the content of the dictionary generated by the Instructor class is as expected"""

        fa = Repository('C:/Users/Dhaval/Documents/ssw_810/hw10/test')

        d = {
            'SSW 567': [
                '98765', 'Einstein, A', 'SFEN'], 'SSW 564': [
                '98764', 'Feynman, R', 'SFEN'], 'SSW 687': [
                '98764', 'Feynman, R', 'SFEN'], 'CS 501': [
                    '98764', 'Feynman, R', 'SFEN']}

        d2 = {'SSW 567': 2, 'SSW 564': 2, 'SSW 687': 1, 'CS 501': 1}

        self.assertDictEqual(fa.instructor.summary, d)
        self.assertDictEqual(fa.instructor.courseInfo, d2)

        with self.assertRaises(FileNotFoundError):
            Repository('C:/Users/Dhaval/Documents/ssw_810/hw9/mehmeh')

        fa.instructor.pretty_print()

    def test_pretty_print_Major(self):
        """checks whether the content of the dictionary generated for Major is as expected"""

        fa = Repository('C:/Users/Dhaval/Documents/ssw_810/hw10/data')

        d = {
            'SFEN': ['SSW 540', 'SSW 564', 'SSW 555', 'SSW 567']
        }

        self.assertEqual(fa.student.core_summary['SFEN'], d['SFEN'])

        d = {
            'SFEN': ['CS 501', 'CS 513', 'CS 545']
        }

        self.assertEqual(fa.student.elective_summary['SFEN'], d['SFEN'])

        fa.student.pretty_printMajor()


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)