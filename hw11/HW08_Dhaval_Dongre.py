from datetime import datetime, timedelta
import os
from collections import defaultdict
from prettytable import PrettyTable


def date_arithmetic():
    """ returns date three days after Feb 27, 2000, Feb 27, 2017 and number of days between Jan1, 2017 and Oct 31, 2017 """
    three_days_after_02272000 = datetime.strptime(
        'Feb 27, 2000', "%b %d, %Y") + timedelta(days=3)
    three_days_after_02272017 = datetime.strptime(
        'Feb 27, 2017', "%b %d, %Y") + timedelta(days=3)
    days_passed_01012017_10312017 = (
        datetime.strptime(
            'Oct 31, 2017',
            "%b %d, %Y") -
        datetime.strptime(
            'Jan 1, 2017',
            "%b %d, %Y")).days

    return three_days_after_02272000, three_days_after_02272017, days_passed_01012017_10312017


def file_reading_gen(path, fields, sep=',', header=False):
    """returns a tuple containing values which are separated by either a comma(,) or a pipe(|)"""

    lineCount = 1
    try:
        fp = open(path, 'r')

    except FileNotFoundError:
        raise

    else:
        with fp:
            if header:
                next(fp)

            for line in fp:
                values = line.rstrip('\n').split(sep)

                if len(values) != fields:
                    raise ValueError(
                        f'{os.path.basename(path)} has {len(values)} fields on line {lineCount} but expected {fields}')

                lineCount += 1
                yield tuple(values)


class FileAnalyzer():
    """ class which reads the content from py files, put data in a dictionary and prints it"""

    def __init__(self, directory):
        """ initialises FileAnalyzer objects"""
        self.directory = directory
        self.files_summary = defaultdict(dict)

        self.analyze_files()  # summerize the python files data

    def analyze_files(self):
        """analyses the files and fills the dictionary we created with content"""
        for file in os.listdir(self.directory):
            if file.endswith(".py"):
                self.files_summary[file] = {}
                self.files_summary[file]['line'] = sum(
                    1 for line in open(os.path.join(self.directory, file)))
                defCount = 0
                classCount = 0
                with open(os.path.join(self.directory, file)) as infile:

                    data = infile.read()
                    characters = len(data)
                    infile.close()

                with open(os.path.join(self.directory, file)) as infile:
                    for line in infile:
                        line = line.strip('\n')
                        wordslist = line.split()

                        if 'def' in wordslist and line.endswith(':'):
                            defCount = defCount + 1
                        if 'class' in wordslist and line.endswith(':'):
                            classCount = classCount + 1

                    self.files_summary[file]['function'] = defCount
                    self.files_summary[file]['class'] = classCount
                    self.files_summary[file]['char'] = characters

    def pretty_print(self):
        """ prints the file name, class count, function count, no of lines and no of characters in each py file"""
        x = PrettyTable()
        x.field_names = [
            "File Name",
            "Classes",
            "Functions",
            "Lines",
            "Characters"]

        for k1, v1 in self.files_summary.items():
            l = list()
            l.append(k1)
            l.append(v1['class'])
            l.append(v1['function'])
            l.append(v1['line'])
            l.append(v1['char'])
            x.add_row(l)

        print(x)


def foo(x, use_max=True, *values):
    #   return x + (min(values) if use_max else max(values))
    if 2:
        return 'yoyoyo'
    else:
        return 'nonono'


def areaRightTriangle(height, width):
    return (height * width) / 2


if __name__ == '__main__':
    # print(date_arithmetic())
    # print(
    #     list(
    #         file_reading_gen(
    #             'C:/Users/Dhaval/Documents/ssw_810/hw8/student_majors.txt',
    #             3,
    #             True,
    #             '|')))
    # fa = FileAnalyzer('C:/Users/Dhaval/Documents/ssw_810/hw8/test')
    # print(fa.files_summary.items())
    # fa.pretty_print()
    # print(foo(1, 2, 3, 4))
    # print(foo(1, False, 3, 4))
    print(foo(1, True, 3, 4))
