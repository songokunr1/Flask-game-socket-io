from flask import Flask, render_template, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from forms import *
from models import *
from flask_socketio import SocketIO, send
from game import *

from flask_session import Session

app = Flask(__name__)
app.secret_key = 'it is hard to hack!'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# app.config['SESSION_TYPE'] = 'filesystem'

# Session(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jlbogoeijkdgra:f66d70134f07635fe3a7106c186ac24b6042b0beef003dec056247d512d21c2d@ec2-79-125-59-247.eu-west-1.compute.amazonaws.com:5432/d7ekrn4ndm767n'
#psql link_to_postgres_heroku
#CREATE TABLE users (
# id SERIAL PRIMARY KEY,
# username VARCHAR (25) UNIQUE NOT NULL
# password TEXT NOT NULL
# );
# \dt
# \d users

db = SQLAlchemy(app)

# socketio = SocketIO(app)
socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=True)
#Flask-SocketIO
# events:
# connect
# disconnect
# message
#JSON

@app.route("/", methods=['GET', 'POST'])
def index():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        user_object = User.query.filter_by(username=username).first()
        if user_object:
            return "Someone else has taken this username!"

        user = User(username=username, password= password)
        db.session.add(user)
        db.session.commit()
        return "inserted into DB!"
    return render_template("index.html", form=reg_form)


@socketio.on('message')
def message(data):
    print(f"\n\n{data}")
    send(data)


@app.route("/start_gra", methods=['POST', "GET"])
def start_gry():

   global gra
   gra = Game()
   gra.init_game()
   # gra.start_gry()
   return redirect(
      url_for('gra'))

@app.route("/gra", methods=['POST', "GET"])
def gra():
    global gra
    print(gra)
    print(gra.gracze)
    karty_gracza = gra.gracze[gra.turn].karty_gracza
    form = WybierzKarte()
    print(form.validate_on_submit())
    print(form.potwierdz.data,form.karta.data)
    # choice_form = ChooseCard(gra.gracze[gra.turn].karty_gracza)
    if form.validate_on_submit():
        gra.ruch()
        return redirect(url_for("gra"))
    return render_template("gra.html", karty_gracza=karty_gracza, form=form)


@app.route('/in')
def testio():
    return render_template("layout.html")

@socketio.on('message')
def message(data):
    print(f'{data}')
    send(data)



if __name__ == "__main__":  # it will vaildate only when file will be executed directly
    app.debug=True
    socketio.run(app)
