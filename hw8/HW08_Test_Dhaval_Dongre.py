import unittest
from HW08_Dhaval_Dongre import date_arithmetic, file_reading_gen
from HW08_Dhaval_Dongre import FileAnalyzer
from datetime import datetime


class TestModuleGeneratorFile(unittest.TestCase):

    def test_date_arithmetic(self):
        """verifies whether the date arithmetic is calculated as expected by thr date_arithmetic function"""
        self.assertEqual(
            date_arithmetic(), (datetime(
                2000, 3, 1, 0, 0), datetime(
                2017, 3, 2, 0, 0), 303))

    def test_file_reading_gen(self):
        """verifies whether the file_reading_gen method correctly extracts data from a file containing comma separated values"""
        self.assertEqual(
            list(
                file_reading_gen(
                    'C:/Users/Dhaval/Documents/ssw_810/hw8/student_majors.txt',
                    3,
                    True,
                    '|')),
            [
                ('123',
                 'Jin He',
                 'Computer Science'),
                ('234',
                 'Nanda Koka',
                 'Software Engineering'),
                ('345',
                 'Benji Cai',
                 'Software Engineering')])

    def test_pretty_print(self):
        """checks whether the content of the dictionary generated by the FileAnalyzer class is as expected"""
        fa = FileAnalyzer('C:/Users/Dhaval/Documents/ssw_810/hw8/test')
        d = {
            '0_defs_in_this_file.py': {
                'line': 3,
                'function': 0,
                'class': 0,
                'char': 57},
            'file1.py': {
                'line': 25,
                'function': 4,
                'class': 2,
                'char': 270}}
        # self.assertEqual(fa.files_summary.items(),d.items())
        # self.assertTrue(fa.files_summary['0_defs_in_this_file.py']==d['0_defs_in_this_file.py'])
        self.assertDictEqual(fa.files_summary, d)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)