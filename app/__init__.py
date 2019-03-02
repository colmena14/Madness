from flask import Flask
from app.controllers import index

def create_app():
    app = Flask(__name__)
    app.register_blueprint(index.bp)

    return app