from flask_smorest import Blueprint

bp = Blueprint('levels', __name__, url_prefix='/level')

from . import routes