from app import db

from werkzeug.security import generate_password_hash, check_password_hash


followers = db.Table('followers',
  db.Column('follower_id', db.Integer, db.ForeignKey('students.id')),
  db.Column('followed_id', db.Integer, db.ForeignKey('students.id'))           
)

class LevelModel(db.Model):

  __tablename__  = 'students'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String, unique = True, nullable = False)
  email = db.Column(db.String, unique = True, nullable = False)
  password_hash = db.Column(db.String, nullable = False)
  first_name = db.Column(db.String)
  last_name = db.Column(db.String)
  levels = db.relationship('LevelModel', backref='author', lazy='dynamic', cascade='all, delete')
  followed = db.relationship('StudentModel', 
    secondary=followers, 
    primaryjoin = followers.c.follower_id == id,
    secondaryjoin = followers.c.followed_id == id,
    backref = db.backref('followers', lazy='dynamic'),
    lazy='dynamic' 
  )

  def __repr__(self):
    return f'<Student: {self.username}>'
  
  def hash_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)
  
  def from_dict(self, dict):
    password = dict.pop('password')
    self.hash_password(password)
    for k,v in dict.items():
      setattr(self, k, v)

  def save(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def is_following(self, student):
    return self.followed.filter(student.id == followers.c.followed_id).count() > 0
  
  def follow_student(self, student):
    if not self.is_following(student):
      self.followed.append(student)
      self.save()

  def unfollow_student(self, student):
    if self.is_following(student):
      self.followed.remove(student)
      self.save()