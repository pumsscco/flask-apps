from .models import Attendance

from flask import render_template
from . import app

@app.route('/')
def index():
    return render_template('templates/index.html')


