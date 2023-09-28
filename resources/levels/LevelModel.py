from app import db
from datetime import datetime

class LevelModel(db.Model):

  __tablename__ = 'levels'

  id = db.Column(db.Integer, primary_key = True)
  body = db.Column(db.String, nullable = False)
  timestamp = db.Column(db.String, default = datetime.utcnow)
  student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable = False)

  def __repr__(self):
    return f'<Level: {self.body}>'
  
  def save(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()