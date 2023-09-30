from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from Config import Config
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

from resources.students import bp as student_bp
api.register_blueprint(student_bp)
from resources.levels import bp as level_bp
api.register_blueprint(level_bp)

from resources.students import routes
from resources.levels import routes


from resources.students.Studentmodel import StudentModel
from resources.levels.LevelModel import LevelModel
