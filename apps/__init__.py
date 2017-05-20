from flask import Flask, render_template, request, jsonify, make_response
from apps.database import db_session
from apps.models import User

app = Flask(__name__)

userDatabase = list()

for ud in User.query.all():
    userDatabase.append(str(ud))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/trylogin")
def trylogin():
    id = request.args.get('id')
    pw = request.args.get('pw')

    if "<{0}, {1}>".format(id, pw) in userDatabase:
        return jsonify(result="true")
    else:
        return jsonify(result="false")
