#  -*- coding:utf-8 -*-
import flask
from flask.ext.sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config.from_object("config")
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'
db = SQLAlchemy(app)


from app import views,models