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

@app.route('/rec/latest')
def latest():
    return render_template('rec/latest.html', rec=rec)

@app.route('/rec/last-week')
def last_week():
    return render_template('rec/last-week.html', recs=recs)

@app.route('/rec/last-month')
def last_month():
    return render_template('rec/last-month.html', recs=recs)