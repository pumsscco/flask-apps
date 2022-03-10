# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Attendance(db.Model):
    __tablename__ = 'attendance'

    id = db.Column(db.Integer, primary_key=True)
    checkin = db.Column(db.DateTime, nullable=False, unique=True, info='打上班卡时间')
    checkout = db.Column(db.DateTime, nullable=False, unique=True, info='打下班卡时间')
    comments = db.Column(db.String(256), server_default=db.FetchedValue(), info='备注')
