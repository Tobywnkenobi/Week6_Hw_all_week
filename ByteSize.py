from flask import Flask, request
from app import app

app = Flask(__name__)

@app.route('/index')
def index():
    return 'Byte Size High'

students = [
    {
        'username':'Kaimo',
        'email':'kaimo@lhs.com',
        'st_level':[{'level':'determining point level'}]
    },
    {
        'username':'Cicimo',
        'email':'cicimo@lhs.com',
        'st_level':[{'level':'determination for point level'}]
    },
]

@app.get('/students')
def get_students():
    return{'students': students}

@app.post('/students')
def create_student():
    student_data = request.get_json()
    student_data['levels'] = []
    students.append(student_data)
    return student_data, 201
    
    
@app.put('/students')
def update_student():
    student = list(filter(lambda student: student["username"] == student_data['username'],students))[0]
    student['username'] = student_data['new username']
    return student, 200

@app.delete('/students')
def delete_user():
    student_data = request.get_json()
    for student in students:
        if student['username'] == student_data['username']:
            student.pop(i)
            print(student)
    return {'message':f'{student_data["username"]} deleted'}, 202