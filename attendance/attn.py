#from flask import Flask, url_for, render_template
from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
from flask_moment import Moment
#----先把表单相关的模块加入进来，后面会用到的
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
#----end
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
#from sqlalchemy.sql import func
from sqlalchemy import func
from datetime import date, datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YHXPUNEK4TCVJHVD9P97CE3WQRAARPXX'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://flask:bTzxVYVt5PQT2SgsJ4JzjNEW@mysql/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False

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
    
    def to_json(self):
        checkin_key='打上班卡时间'
        checkout_key='打下班卡时间'
        comments_key='备注'
        json_attn = {
            checkin_key: self.checkin.strftime('%Y年%m月%d日 %H时%M分%S秒'),
            checkout_key: self.checkout.strftime('%Y年%m月%d日 %H时%M分%S秒'),
            comments_key: self.comments
        }
        return json_attn
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rec/latest')
def latest():
    rec=Attendance.query.order_by(Attendance.checkin.desc()).first()
    return render_template('rec/latest.html', rec=rec)

@app.route('/api/rec/latest')
def api_latest():
    rec=Attendance.query.order_by(Attendance.checkin.desc()).first()
    return jsonify(rec.to_json())

def last_week():
    NOW=datetime.now()
    recs=Attendance.query.filter(
        Attendance.checkin>NOW-timedelta(days=7)).order_by(
        Attendance.checkin.desc()).all()
    return recs

@app.route('/rec/last-week')
def web_last_week():
    recs=last_week()
    return render_template('rec/last-week.html', recs=recs)

@app.route('/api/rec/last-week')
def api_last_week():
    recs=last_week()
    json_list=[rec.to_json() for rec in recs]
    return jsonify(json_list)

#近一个月记录
def last_month():
    recs=Attendance.query.filter(
        Attendance.checkin>text('NOW() - INTERVAL 1 MONTH')).order_by(
        Attendance.checkin.desc())
    return recs
##直接输出到网页
@app.route('/rec/last-month')
def web_last_month():
    res=last_month()
    page = request.args.get('page', 1, type=int)
    pagination=res.paginate(page, per_page=5, error_out=False)
    recs = pagination.items
    return render_template('rec/last-month.html', recs=recs,pagination=pagination)
##输出为json，供api调用
@app.route('/api/rec/last-month')
def api_last_month():
    recs=last_month().all()
    json_list=[rec.to_json() for rec in recs]
    return jsonify(json_list)

'''SELECT year(checkin),month(checkin),
        sum(hour(timediff(checkout,checkin))+minute(timediff(checkout,checkin))/60)
        FROM attendance group by year(checkin),month(checkin)'''
'''
Attendance.query(
    func.year(Attendance.checkin), 
    func.month(Attendance.checkin)
).filter(
    Attendance.checkin>='2022-06-06'
).order_by(
    Attendance.checkin.desc()
)
'''
def month_json(stat):
    y='年'
    m='月'
    h='工时'
    json_mon = {
        y: stat.year,
        m: stat.month,
        h: stat.hours
    }
    return json_mon

@app.route('/api/stat/month')
def month_hour():
    month_stats=Attendance.query.with_entities(
        func.year(Attendance.checkin).label("year"), 
        func.month(Attendance.checkin).label("month"), 
        func.sum(
            func.hour(
                func.timediff(Attendance.checkout, Attendance.checkin)
            )+func.minute(
                func.timediff(Attendance.checkout, Attendance.checkin)
            ).label("hours")
        ) / 60
    ).group_by(
        func.year(Attendance.checkin), 
        func.month(Attendance.checkout)
    ).order_by(year,month)
    '''month_stats=Attendance.query.with_entities(
        func.year(Attendance.checkin).label("year"), 
        func.month(Attendance.checkin).label("month")
    ).filter(
        Attendance.checkin>='2022-07-01'
    ).order_by(
        Attendance.checkin.desc()
    ).all()'''
    json_list=[month_json(month_stat) for month_stat in month_stats]
    return jsonify(json_list)

