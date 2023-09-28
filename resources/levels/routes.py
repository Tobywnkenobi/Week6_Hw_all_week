from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort
from sqlalchemy.exc import IntegrityError

from resources.Students.models import StudentModel

from .LevelModel import LevelModel
from schemas import LevelSchema
from . import bp

@bp.route('/')
class LevelList(MethodView):
  
  @bp.response(200, LevelSchema(many=True))
  def get(self):
    return LevelModel.query.all()

  @bp.arguments(LevelSchema)
  @bp.response(200, LevelSchema)
  def level(self, level_data):
    p = LevelModel(**level_data)
    u = StudentModel.query.get(level_data['student_id'])
    if u:
      p.save()
      return p
    else:
      abort(400, message="Invalid Student Id")

@bp.route('/<level_id>')
class Level(MethodView):
  
  @bp.response(200, LevelSchema)
  def get(self, level_id):
    p = LevelModel.query.get(level_id)
    if p:
      return p
    abort(400, message='Invalid Level Id')

  @bp.arguments(LevelSchema)
  @bp.response(200, LevelSchema)
  def put(self, level_data, level_id):
    p = LevelModel.query.get(level_id)
    if p and level_data['body']:
      if p.student_id == level_data['student_id']:
        p.body = level_data['body']
        p.save()
        return p
    abort(400, message='Invalid Level Data')

  def delete(self, level_id):
     req_data = request.get_json()
     student_id = req_data['student_id']
     p = LevelModel.query.get(level_id)
     if p:
       if p.student_id == student_id:
        p.delete()
        return {'message' : 'Level Deleted'}, 202
       abort(400, message='User doesn\'t have rights')
     abort(400, message='Invalid Level Id')
