#from flask import Flask, url_for, render_template
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html')
