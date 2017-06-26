# --coding:utf-8 --
from app import app
from flask import render_template,request

@app.route("/")
@app.route("/index")
def index():
	user = {"nickname":"Flask"}
	posts = [{"author":{"nickname":"John"},"body":"beautiful day in portland"},
			 {"author":{"nickname":"Susan"},"body":"The Avengers movie was so cool"}]
	return render_template("index.html",title="Home",user=user,posts=posts)


@app.route("/services")
def services():
	return "Services"

@app.route("/about")
@app.route("/info")
def about():
	return "About"

@app.route("/user/<username>")
def user(username):
	return "username %s" % username

@app.route("/login",methods=["GET","POST"])
def login():
	if request.method == "POST":
		username=request.form["username"]
		password=request.form["password"]
		return render_template("login.html",method=request.method)
	else:
		return render_template("login.html",method=request.method)

