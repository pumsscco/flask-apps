#from flask import Flask, url_for, render_template
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
#----先把表单相关的模块加入进来，后面会用到的
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
#----end
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from datetime import date, datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YHXPUNEK4TCVJHVD9P97CE3WQRAARPXX'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://flask:bTzxVYVt5PQT2SgsJ4JzjNEW@mysql/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap(app)
moment = Moment(app)
db=SQLAlchemy(app)

class Attendance(db.Model):
    __tablename__ = 'attendance'

    id = db.Column(db.Integer, primary_key=True)
    checkin = db.Column(db.DateTime, nullable=False, unique=True, info='打上班卡时间')
    checkout = db.Column(db.DateTime, nullable=False, unique=True, info='打下班卡时间')
    comments = db.Column(db.String(256), server_default=db.FetchedValue(), info='备注')
    
    def __repr__(self):
        return '<<考勤记录： %r, %r, %r >>' % (self.checkin, self.checkout, self.comments)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rec/latest')
def latest():
    rec=Attendance.query.order_by(Attendance.checkin.desc()).first()
    return render_template('rec/latest.html', rec=rec)

@app.route('/rec/last-week')
def last_week():
    NOW=datetime.now()
    recs=Attendance.query.filter(
        Attendance.checkin>NOW-timedelta(days=7)).order_by(
        Attendance.checkin.desc()).all()
    return render_template('rec/last-week.html', recs=recs)

@app.route('/rec/last-month')
def last_month():
    #NOW=datetime.now()
    page = request.args.get('page', 1, type=int)
    pagination=Attendance.query.filter(
        Attendance.checkin>text('NOW() - INTERVAL 1 MONTH')).order_by(
        Attendance.checkin.desc()).paginate(
        page, per_page=5, error_out=False)
    recs = pagination.items
    return render_template('rec/last-month.html', recs=recs,pagination=pagination)