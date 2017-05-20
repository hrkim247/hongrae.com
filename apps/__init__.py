from flask import Flask, render_template, request, jsonify, make_response, session
from apps.database import db_session
from apps.models import User

app = Flask(__name__)

app.secret_key = b'\xddl@C\xf08s\xa4\xba\xcf_o%r\x94\xe0\xdc\x94\x8aL\xef=\xc4\x1d'

userDatabase = list()

for ud in User.query.all():
    userDatabase.append(str(ud))

def loginConfirm(template):
    try:
        if session["user"] in userDatabase:
            return render_template(template, login=True)
        else:
            return render_template(template, login=False)
    except KeyError:
        return render_template(template, login=False)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route("/")
def index():
    return loginConfirm("index.html")

@app.route("/login")
def login():
    return loginConfirm("login.html")

@app.route("/trylogin")
def trylogin():
    id = request.args.get('id')
    pw = request.args.get('pw')

    userFormat = "<{0}, {1}>".format(id, pw)

    if  userFormat in userDatabase:
        session["user"] = userFormat
        return jsonify(result="true")
    else:
        return jsonify(result="false")

@app.route("/trylogout")
def trylogout():
    logout = request.args.get("logout")

    if logout == "true":
        print(session)
        session.pop("user", None)
        return jsonify(result="true")
