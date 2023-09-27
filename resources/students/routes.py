from flask import request
from uuid import uuid4

from . import bp
from db import students, level

@bp.get('/student')
def get_student():
  return {'student': students}, 200

@bp.get('/student/<student_id>')
def get_student(student_id):
  try:
    student = student[student_id]
    return student, 200
  except KeyError:
    return {'message': 'user not found'}, 400

@bp.post('/student')
def create_student():
  student_data = request.get_json()
  student[uuid4().hex] = student_data
  return student_data, 201

@bp.put('/student/<student_id>')
def update_student(student_id):
  student_data = request.get_json()
  try:
    student = student[student_id]
    student['username'] = student_data['username']
    return student, 200
  except KeyError:
    return {'message': 'user not found'}, 400

@bp.delete('/student')
def delete_students():
  user_student = request.get_json()
  for i, student in enumerate(students):
    if student['username'] == student_data['username']:
      students.pop(i)
      print(students)
  return {'message':f'{student_data["username"]} deleted'}, 202

@bp.get('/student/<student_id>/post')
def get_student_posts(student_id):
  if student_id not in students:
    return {'message': 'user not found'}, 400
  student_posts = [level for levels in level.values() if level['student_id'] == student_id]
  return student_levels, 200