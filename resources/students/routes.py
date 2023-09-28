from flask.views import MethodView
from flask_smorest import abort
from sqlalchemy.exc import IntegrityError

from schemas import LevelSchema, UpdateStudentSchema, StudentSchema, DeleteStudentSchema, StudentSchemaNested
from . import bp
from .models import StudentModel

@bp.route('/student')
class StudentList(MethodView):  
  
  @bp.response(200, StudentSchema(many = True))
  def get(self):
    students = StudentModel.query.all()
    return students

  @bp.arguments(StudentSchema)
  @bp.response(201, StudentSchema)
  def post(self, student_data):
    student = StudentModel()
    student.from_dict(student_data)
    try:
      student.save()
      return student_data
    except IntegrityError:
      abort(400, message='Username or Email already Taken')

  @bp.arguments(DeleteStudentSchema)
  def delete(self, student_data):
    student = StudentModel.query.filter_by(username=student_data['username']).first()
    if student and student.check_password(student_data['password']):
      student.delete()
      return {'message':f'{student_data["username"]} deleted'}, 202
    abort(400, message='Username or Password Invalid')

@bp.route('/student/<student_id>')
class Student(MethodView):

  @bp.response(200, StudentSchemaNested)
  def get(self, student_id):
    student = StudentModel.query.get_or_404(student_id, description='Student Not Found')
    return student

  @bp.arguments(UpdateStudentSchema)
  @bp.response(202, StudentSchema)
  def put(self, student_data, student_id):
    student = StudentModel.query.get_or_404(student_id, description='Student Not Found')
    if student and student.check_password(student_data['password']):
      try:
        student.from_dict(student_data)
        student.save()
        return student
      except IntegrityError:
        abort(400, message='Username or Email already Taken')


@bp.route('/student/follow/<follower_id>/<followed_id>')
class FollowUser(MethodView):
  
  @bp.response(200, StudentSchema(many=True))
  def post(self, follower_id, followed_id):
    student = StudentModel.query.get(follower_id)
    student_to_follow = StudentModel.query.get(followed_id)
    if student and student_to_follow:
      student.follow_user(student_to_follow)
      return student.followed.all()
    abort(400, message='Invalid student info')

  def put(self, follower_id, followed_id):
    student = StudentModel.query.get(follower_id)
    student_to_unfollow = StudentModel.query.get(followed_id)
    if student and student_to_unfollow:
      student.unfollow_user(student_to_unfollow)
      return {'message': f'Student: {student_to_unfollow.username} unfollowed'}, 202
    abort(400, message='Invalid student info')  