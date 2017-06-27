# --coding:utf-8 --
from app import app
from flask import render_template,request,url_for,redirect
from werkzeug.utils import secure_filename
from os import path

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

@app.route("/upload",methods=["POST","GET"])
def upload():
	if request.method == "POST":
		f = request.files["file"]
		basefile = path.abspath(path.dirname(__file__))
		uploadpath = path.join(basefile,"static/upload")
		f.save(uploadpath,secure_filename(f.filename))
		return redirect(url_for("upload"))
	return render_template("upload.html")

