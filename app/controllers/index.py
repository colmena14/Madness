from flask import Blueprint, render_template

from app.db import db
from app.models.team import Team

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/', methods=('GET',))
def index():
    teams = Team.query.all()
    return render_template('index.html', name='Adam', teams=teams)