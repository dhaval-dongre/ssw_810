from HW08_Dhaval_Dongre import file_reading_gen
import os
from collections import defaultdict
from prettytable import PrettyTable


class Repository:
    """a container class which encapsulates info for class Student and Instructor"""

    def __init__(self, directory):
        self.directory = directory
        self.student = self.Student(directory)
        self.instructor = self.Instructor(directory)
                

    class Student:
        """contains info for students and stores information regarding their id's, courses and grades"""

        def __init__(self, directory):
            self.gradesList = defaultdict(str)
            self.summary = defaultdict()
            self.core_summary=defaultdict()
            self.elective_summary=defaultdict()
            self.directory=directory
            

            self.core_summary=defaultdict()
            self.elective_summary=defaultdict()
            count=0

            for l in file_reading_gen(
                    os.path.join(
                        directory,
                        'majors.txt'),
                    3,
                    '\t',
                    True):

                if l[0] not in self.core_summary.keys():
                    self.core_summary[l[0]] = list()
                    self.elective_summary[l[0]] = list()

                # count+=1

                if l[1]=='R':
                    self.core_summary[l[0]].append(l[2])
                else:
                    self.elective_summary[l[0]].append(l[2])

            gList = list(
                file_reading_gen(
                    os.path.join(
                        directory,
                        'grades.txt'),
                    4,
                    '|',True))

            for l in file_reading_gen(
                    os.path.join(
                        directory,
                        'students.txt'),
                    3,
                    ';', True):
                self.summary[l[0]] = list()
                self.summary[l[0]].append(l[1])
                courseList = list()
                for g in gList:
                    if l[0] == g[0]:
                        self.gradesList[g[1]] = g[2]
                        courseList.append(g[1])
                self.summary[l[0]].extend(sorted(courseList))

        def pretty_print(self):
            """ prints the cwid, name and courses for each student"""
            x = PrettyTable()
            x.field_names = [
                "CWID",
                "Name",
                "Completed Courses",
                "Remaining Required",
                "Remaining Electives"
            ]

            passing_grades = {'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C'}

            gList = list(
                file_reading_gen(
                    os.path.join(
                        self.directory,
                        'grades.txt'),
                    4,
                    '|'))

            for k1, v1 in self.summary.items():
                l = list()
                l.append(k1)
                l.append(v1[0])
                l.append(v1[1:])

                yo1=self.core_summary[v1[1]]
                yo2=list(v1[2:])
                core=self.core_summary[v1[1]]-list(v1[2:])

                for c in core:

                    for g in gList:
                        if g[1]==c and g[0]==k1:

                            if g[2] not in passing_grades:
                                core.remove(c)
                                break

                l.append(core)

                elective=self.elective_summary[v1[1]]-list(v1[2:])

                for c in elective:

                    for g in gList:
                        if g[1]==c and g[0]==k1:

                            if g[2] not in passing_grades:
                                elective.remove(c)
                                break

                        
                l.append(elective)
                x.add_row(l)

            print('\n')
            print(x)

    class Instructor:
        """class containing information for Instructors and stores information regarding their cwid, name, dept, course etc"""

        def __init__(self, directory):
            self.summary = defaultdict()
            self.courseInfo = defaultdict(int)

            gList = list(
                file_reading_gen(
                    os.path.join(
                        directory,
                        'grades.txt'),
                    4,
                    '|',True))

            for l in file_reading_gen(
                    os.path.join(
                        directory,
                        'instructors.txt'),
                    3,
                    '|',True):

                for g in gList:
                    if l[0] == g[3]:
                        self.summary[g[1]] = list()
                        self.summary[g[1]].append(g[3])
                        self.summary[g[1]].append(l[1])
                        self.summary[g[1]].append(l[2])
                        self.courseInfo[g[1]] += 1

        def pretty_print(self):
            """ prints the instructor cwid, name, dept, course and no of students"""
            x = PrettyTable()
            x.field_names = [
                "CWID",
                "Name",
                "Dept",
                "Course",
                "Students"
            ]

            for k1, v1 in self.summary.items():
                l = list()
                l.append(v1[0])
                l.append(v1[1])
                l.append(v1[2])
                l.append(k1)
                l.append(self.courseInfo[k1])
                x.add_row(l)

            print('\n')
            print(x)


if __name__ == '__main__':
    r = Repository('C:/Users/Dhaval/Documents/ssw_810/hw10/data/')
    r.student.pretty_print()
    r.instructor.pretty_print()
