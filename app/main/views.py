from flask import render_template

from .. import db
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', message='Welcome to your Flask App')
