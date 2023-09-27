from flask import request
from uuid import uuid4

from app import app

from db import posts

@app.get('/level')
def get_levels():
  return {'levels': posts}

@app.get('/level/<level_id>')
def get_level(level_id):
  try:
    level = levels[level_id]
    return level, 200
  except KeyError:
    return {'message': 'post not found'}, 400

@app.post('/level')
def create_level():
  level_data = request.get_json()
  levels[uuid4().hex] = level_data
  return level_data, 201

@app.put('/level/<level_id>')
def edit_level(level_id):
  level_data = request.get_json()
  if level_id in levels:
    level = levels[level_id]
    level['body'] = level_data['body']
    return level, 200
  return {'message': 'Post not found'}, 400

@app.delete('/level/<level_id>')
def delete_level(level_id):
  try:
    deleted_level = levels.pop(level_id)
    return {'message':f'{deleted_level["body"]} deleted'}, 202
  except KeyError:
    return {'message': 'Post not found'}, 400
