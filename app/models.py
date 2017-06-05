#	-- coding:utf-8 --

from app import db

class user(db.Model):
	__tablename__ = "first"

	id = db.Column(db.Integer,primary_key=True)
	nickname = db.Column(db.String(64))
	email = db.Column(db.String(120))

	def __repr__(self):
		return "<User %r>" % (self.nickname)


row1 = user(nickname="chlv",email="lc1923@live.cn")
row2 = user(nickname="Iron_man",email="unknow")
row3 = user(nickname="star_man",email="unknow")

db.session.add_all([row1,row2,row3])
db.session.commit()