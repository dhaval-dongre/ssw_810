from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def yo():
    return "Hey There! Hope you are having a wonderful day!"

@app.route('/instructors')
def instructors():

    query='select instructors.CWID, instructors.Name, instructors.Dept, grades.Course, count(Course) as Count from instructors join grades on InstructorCWID=CWID group by InstructorCWID, instructors.Name, instructors.Dept, grades.Course'

    connect = sqlite3.connect('data/hw11.db')

    rows=connect.execute(query)

    data = [{'cwid': cwid, 'name': name, 'department': department, 'courses': courses, 'students': students} for cwid, name, department, courses, students in rows]

    connect.close()

    return render_template('instructors.html', title="Stevens Repository", table_title="No. of students by course and instructor", instructors=data)

if __name__ == '__main__':
    app.run(debug=True)