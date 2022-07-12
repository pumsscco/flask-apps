from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://flask:bTzxVYVt5PQT2SgsJ4JzjNEW@mysql/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)
db = SQLAlchemy()
db.init_app(app)
bootstrap=Bootstrap()
bootstrap.init_app(app)

