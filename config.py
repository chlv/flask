#		-- coding:utf-8 --

import os
HOST = "127.0.0.1"
PORT = "3307"
USERNAME = "root"
PASSWORD = "root"
DBNAME = "flask"



basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir,"app.db")
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,"flask_db_ext")
