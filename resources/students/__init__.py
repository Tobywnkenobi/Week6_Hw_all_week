from flask_smorest import Blueprint

bp = Blueprint('students', __name__, description='Ops on Students')

from . import routes
