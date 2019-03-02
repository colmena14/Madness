from flask import Flask

from app.controllers import index
from app.models.team import Team
from app.db import db

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

    db.init_app(app)

    @app.before_first_request
    def create_db():
        db.create_all()

    app.register_blueprint(index.bp)

    return app