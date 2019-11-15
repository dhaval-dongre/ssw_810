import sqlite3                                       
from prettytable import PrettyTable

class DBReader:

    def instructor_table_db(self, db_path):

        labels=['CWID','Name','Department','Courses','Students']

        query='select instructors.CWID, instructors.Name, instructors.Dept, grades.Course, count(Course) as Count from instructors join grades on InstructorCWID=CWID group by InstructorCWID, instructors.Name, instructors.Dept, grades.Course'

        connect = sqlite3.connect(db_path)

        x=PrettyTable(labels)

        for row in connect.execute(query):
            x.add_row(row)

        print(x)


if __name__=='__main__':
    d=DBReader()
    d.instructor_table_db('C:/Users/Dhaval/Documents/ssw_810/hw11/data/hw11.db')                       

