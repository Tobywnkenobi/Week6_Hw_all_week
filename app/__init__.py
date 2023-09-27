from flask import Flask

app = Flask(__name__)


from resources.students import bp as student_bp
app.register_blueprint(student_bp)

from resources.levels import bp as levels_bp
app.register_blueprint(level_bp)

from resources.students import routes
from resources.levels import routes
